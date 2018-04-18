#!/bin/sh

RANCID_DIR="/usr/local/var/rancid/multi-visp"
TFTP_IP="172.16.88.16"

SCRIPT="acl-ios.sh"

IFCONFIG="/sbin/ifconfig"
GREP="/usr/bin/grep"
AWK="/usr/bin/awk"
CAT="/bin/cat"
ECHO="/bin/echo"
TR="/usr/bin/tr"
CLOGIN="/usr/local/libexec/rancid/clogin"
CHMOD="/bin/chmod"

cd $RANCID_DIR 

echo "#!/bin/sh" > $SCRIPT

$CAT << EOF >> $SCRIPT
for i in \`$IFCONFIG | $GREP "inet " | $GREP -v "127.0.0.1" | $AWK '{ print \$2 }'\`;
do
        RESULT=\`$GREP \$i /tftpboot/acl-1\`
        if [ \$? -ne 0 ]
        then
                $ECHO "pas bien"
                exit 1
        fi
done
EOF

DEVICES=`$CAT router.db | $GREP ":cisco:up" | $AWK -F ":" '{ print $1 " " }' | $TR -d '\n\'`
$ECHO $CLOGIN -S -c \"conf t\; file prompt quiet\; exit\; copy tftp://$TFTP_IP/acl-1 running-config\; copy tftp://$TFTP_IP/acl-2 running-config\; conf t\; no file prompt quiet\; exit\" $DEVICES >> $SCRIPT
$CHMOD +x $SCRIPT
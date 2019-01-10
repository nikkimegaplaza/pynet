
from __future__ import unicode_literals, print_function
import re 


with open("show_version.txt") as f:
	show_ver = f.read() #string
	
ver_match = re.search(r"Version (.*),", show_ver)
version = ver_match.group(1)

ser_match = re.search(r'Processor board ID ([A-Z0-9]+)',show_ver)
serial = ser_match.group(1)

conf_match = re.search(r'Configuration register is ([\S]+)',show_ver)
conf = conf_match.group(1)

print()
print('OS Version: {}'.format(version))
print('Serial Number: {}'.format(serial))
print('Config Register: {}'.format(conf))

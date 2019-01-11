
from __future__ import unicode_literals, print_function
import re

with open("show_ipv6_intf.txt") as f:
    output = f.read() #string
	
match = re.search(r'IPv6 address:\s+(.*)IPv6 subnet:' , output, flags = re.DOTALL)
print()
ipv6_add = match.group(1).strip() #string
ipv6_list = ipv6_add.splitlines() #list

ipv6_list_new = [s.replace('[VALID]',' ') for s in ipv6_list] #list
#https://stackoverflow.com/questions/8282553/removing-character-in-list-of-strings

ipv6_list_new = [x.strip(' ') for x in ipv6_list_new]
#https://stackoverflow.com/questions/3232953/python-removing-spaces-from-list-objects

print(ipv6_list_new)

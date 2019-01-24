from __future__ import unicode_literals, print_function
import re
import random


#Call your function using no arguments.
def ip_addr(ip = '10.10.10.'):
	x = str(random.randint(1,254)) #int -> str
	return(ip + x)

print()
#Call your function using no arguments.
print(ip_addr())
#Call your function using a positional argument.
print(ip_addr('192.168.2.'))
#Call your function using a named argument.
print(ip_addr(ip = '172.16.31.'))
print()


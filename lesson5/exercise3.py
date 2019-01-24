from __future__ import unicode_literals, print_function
import re
import random


def mac(mac_addr):
	
	mac_addr = mac_addr.upper()
	
	if ':' in mac_addr or '-' in mac_addr:
		new_mac = [] #list
		octects = re.split(r"[-:]", mac_addr) #list
			#removes the : and creates a list of strings
		for octect in octects:
			if len(octect) <2:
				octect = octect.zfill(2)
				#coverts list to str
				#from ['2', '3', '4', '5', '6'] to 2:3:4:5:6
			new_mac.append(octect)
	elif '.' in mac_addr:
		new_mac = [] 
		sections = mac_addr.split('.') #list of strings
		if len(sections) != 3:
			raise ValueError("something is wrong")
			
		for word in sections:
			if len(word) < 4:
				word = word.zfill(4)
			new_mac.append(word[:2])
			new_mac.append(word[2:])
	return ":".join(new_mac)
		
		
# Some tests
assert "01:23:02:34:04:56" == mac('123.234.456')
assert "AA:BB:CC:DD:EE:FF" == mac('aabb.ccdd.eeff')
assert "0A:0B:0C:0D:0E:0F" == mac('a:b:c:d:e:f')
assert "01:02:0A:0B:03:44" == mac('1:2:a:b:3:44')
assert "0A:0B:0C:0D:0E:0F" == mac('a-b-c-d-e-f')
assert "01:02:0A:0B:03:44" == mac('1-2-a-b-3-44')
print("Tests passed")

'''	MY FAILED CODE
	
	if (mac_addr.find('-') == true) && (len(mac_addr) == 17):
		mac_addr = mac_addr.strip(-)
		for x in mac_addr:
			#conver str to list
			
			
			x+2
		new_mac_addr = str(mac_addr) #convert list to str
	if (mac_addr.find('.') == true) && (len(mac_addr) == 14):
		mac_addr = mac_addr.strip(.)
'''

#!/usr/bin/env python
"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""
from __future__ import unicode_literals, print_function
	

my_dict = {
	"ip_addr": "9.9.9.9",
	"vendor" : "cisco",
	"username" : "admin",
	"password" : "pass"
	}
print()	
print(my_dict["ip_addr"])
print()

if my_dict["vendor"].lower() == "cisco" :
	my_dict["platform"] = "ios"
elif my_dict["vendor"].lower() == "juniper" :
	my_dict["platform"] = "junos:"
	

bgp_fields = {
	'bgp_as' : 42,
	'peer_as' : 100,
	'peer_ip' : '1.1.1.1'
}

my_dict.update(bgp_fields)

print("-" * 50)
for x,y in my_dict.items():
	#print("{key"":>15} {value}".format(key=x,value=y))
	print("{key:>15} ---> {value}".format(key=x, value=y))

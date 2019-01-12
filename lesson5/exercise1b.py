from __future__ import unicode_literals, print_function


def ssh_conn2(ip_addr, username, password, device_type = 'cisco_ios'):
	print('*'*30)
	print("Ip add is {}".format(ip_addr))
	print("Username is {}".format(username))
	print("Password is {}".format(password))
	print("Device type is {}".format(device_type))
	print('*'*30)
		
'''
ssh_conn('10.10.3.9', 'bob', 'cat')
#Call this ssh_conn function using entirely positional arguments.

ssh_conn(ip_addr = '6.7.8.9', username = 'mark', password = 'rainbow')
#Call this ssh_conn function using entirely named arguments.

ssh_conn('2.3.4.5', username = 'mark', password = 'rainbow')
#Call this ssh_conn function using a mix of positional and named arguments.
'''

ssh_conn2('1.1.1.1', 'veronica', 'login')
ssh_conn2('1.1.1.1', 'veronica', 'login', 'nexus')
#this overwrote the default device type

my_device = {
    "ip_addr": "172.16.1.1",
    "device_type": "cisco_xr",
    "username": "admin",
    "password": "cisco123"
}

ssh_conn2(**my_device)

from __future__ import unicode_literals, print_function


def ssh_conn(ip_addr, username, password):
	print('*'*30)
	print("Ip add is {}".format(ip_addr))
	print("Username is {}".format(username))
	print("Password is {}".format(password))
	print('*'*30)
	
ssh_conn('10.10.3.9', 'bob', 'cat')
#Call this ssh_conn function using entirely positional arguments.

ssh_conn(ip_addr = '6.7.8.9', username = 'mark', password = 'rainbow')
#Call this ssh_conn function using entirely named arguments.

ssh_conn('2.3.4.5', username = 'mark', password = 'rainbow')
#Call this ssh_conn function using a mix of positional and named arguments.

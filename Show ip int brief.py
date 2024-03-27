
import json
import textfsm
import os
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
                             "host": '192.168.0.250',
                             "username": 'blake',
                             "password": 'blake',
                             "device_type": 'cisco_ios',
                             "session_log": 'my_session.txt',
                             "secret": 'blake',
                                                          }





net_connect = ConnectHandler(**device1)
ip_int = (net_connect.send_command('show ip int brief', use_textfsm=True))
#print(json.dumps(ip_int, indent=4))

#print(ip_int[0]["interface"] + " has the ip of " + ip_int[0]["ip_address"])

for x in ip_int:
    print("interface " + x['interface'] + ' has the ip of ' + x['ip_address'] )

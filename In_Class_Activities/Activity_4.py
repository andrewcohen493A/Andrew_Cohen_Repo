"""
Andrew Cohen
activity 4
"""
import platform
import os
#MJ: Add comments
ip_address = ["127.0.0.1","8.0.0.1","192.168.0.10","192.168.10.10"]   # list of all ip addresses

for ip_address in ip_address:  # a for ;oop to run through all ip addresses that are placed in the list

    ping_cmd = f"ping -w 2 {ip_address} > ./dev 2>&1"  # python command to execute the ping function

    exit_code = os.system(ping_cmd)

    print(exit_code)

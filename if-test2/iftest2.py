#!/usr/bin/env python3
ipchk_prompt="Please enter the IP address: "
ipchk=input(ipchk_prompt)

if ipchk == '192.168.70.1':
	print('Looks like the IP address of the gateway was set: ' + ipchk + ' This is not recommended')

#if any data is provided it tests true
elif ipchk:
	print('looks like the IP address was set: ' + ipchk)

#if data is no provided
else:
	print("You did not provide input!")

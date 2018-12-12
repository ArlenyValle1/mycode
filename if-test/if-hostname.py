#!/usr/bin/env python3

##prompts user input
prompt_hostname="Please enter a vaue for hostname: "

##set hostname to user input
hostname= (input(prompt_hostname))


##capatalize all user input to ensure it equals stored value
hostname= hostname.upper()

##conditional statement that prints if value entered matches value stored
if hostname == 'MTG':
	print('Hostname matches the expected config')

print("Exiting the script")





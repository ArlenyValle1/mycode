#!/usr/bin/env python3
#initialize promt string
prompt_name_msg="Please enter your full name: "

#input function for name
user_name= input(prompt_name_msg)

#error checking:check that the suer_name is not empty

while (user_name == ''):
#promt the user for their name again
	user_name=input(prompt_name_msg)
#END of the while loop, for USER-NAME initilization

print()
print("Welcome to the wonderful world of python, ", user_name)
print()


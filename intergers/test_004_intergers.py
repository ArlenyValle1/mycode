#!/usr/bin/env python3
prompt_age_msg="Please enter your age"
user_age = int(input(prompt_age_msg))
while(user_age <=0):
	user_age=int(input(prompt_age_msg))

print()
print("Your age is: ", user_age)
print()
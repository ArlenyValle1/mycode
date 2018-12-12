#!/usr/bin/env python3
a_list=[1,2,3,4]
print("The original list...")
print(a_list)
print()

print("Item 1 in the list is: ", a_list[0])
print("Item 2 in the list is: ", a_list[1])
print("Item 3 in the list is: ", a_list[2])
print("Item 4 in the list is: ", a_list[3])
print()
reversed_list=a_list[-1::-1]
##[-1::1] means start at index 1,iterate through all items, but step backward at 1
##[1:3:1] would mean start at index 1, end at index 3 step by 1 (this would be 2,3,4)
#[start:end:step]

print("The reversed list...")
print(reversed_list)
print()

print("Now using the FOR loop to manuever the entire list")

for my_item in reversed_list:
	print(my_item)
##this will print the reversed list vertically



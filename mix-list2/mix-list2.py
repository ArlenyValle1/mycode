#!/usr/bin/env python3
proto= ['ssh', 'http', 'https']
protoa= ['ssh', 'http', 'https']
print (proto)
print (proto[1])
proto.extend('dns') # this line will add 'd', 'n', and 's' to the end of our list
print(proto)
proto2=[22,80,443,53] #a list of command ports
proto.extend(proto2) #pass proto2 to proto using extend method
print(proto)
protoa.append(proto2)#pass proto2 as an argument to the append method
print(protoa)


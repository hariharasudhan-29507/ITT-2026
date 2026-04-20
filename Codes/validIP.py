# Author - Hariharasudhan A

import time # for sleep() // style printing *
import sys # for exit() // flushing blocks

print("  Welcome to IPv4 validation portal\n")
for i in range(37):
   print("*",end="",flush=True)
   time.sleep(0.1)
print("\n\n")

ip=input("enter IP address:")

'''
An IP is valid if and only if the octets are in range of 0 - 255
IPv4 is 4 octet IP set , i.e IP[0] . IP[1] . IP[2] . IP [3] --> 1.1.1.1 
'''
count=0
flag=0
# first checking whether this is a IPv4 or not
for i in range(0,len(ip)):
   if ip[i] in ".":
      count=count+1
if count!=3:
   print("not an IPv4")
   sys.exit()
iplist=ip.split(".")

# validating every octet under range of 0 - 255
for i in range(len(iplist)):
   if int(iplist[i])>=0 and int(iplist[i])<=255 :
      if iplist[i].isnumeric():
         flag=1
   else:
      flag=0
      break
if flag==1:
   print("valid IP address")
else:
   print("not a valid IP address")

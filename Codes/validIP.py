import time
import sys
print("  Welcome to IPv4 validation portal\n")
for i in range(37):
   print("*",end="",flush=True)
   time.sleep(0.1)
print("\n\n")
ip=input("enter IP address:")
count=0
flag=0
for i in range(0,len(ip)):
   if ip[i] in ".":
      count=count+1
if count!=3:
   print("not an IPv4")
   sys.exit()
iplist=ip.split(".")
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

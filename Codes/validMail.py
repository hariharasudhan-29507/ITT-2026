# Author - Hariharasudhan A

import sys # for exit() , for flushing blocks
mail=input("enter mail id :")
l=len(mail.split()) 
if l==0: # to check if mail exists
   print("mail id is a required field (*)")
   sys.exit()
flag=0
try:
   l1=mail.index("@") # before domain @ 
except ValueError:
   print("check your mail once again\n") # exception caught
   l1=0

if l1!=0: # before @ check
   for i in range(l,l1):
      for j in ".#!$%^&*(){}:><?":
         if mail[i].startswith(j) and mail[i].endswith(j): # mail can't have special characters before @
            print("check your mail once again\n")
            sys.exit()
         else:
            flag=1
   try:
      l2=mail.index(".") # after @ check for '.'
   except ValueError:
      print("check your mail once again\n")
      l2=0
   if l2!=0:
      for i in range(l1,l2): # between @ and '.' there should be no integers
         if mail[i] in "9876543210":
            print("check your mail once again")
            sys.exit()
         else:
            flag=1
         l3=l-l2
         for i in range(l3,l):
            if mail[i] in "9876543210":
               print("check your mail once again")
               sys.exit()
            else:
               flag=1

if flag==1:
   print("this mail is valid")

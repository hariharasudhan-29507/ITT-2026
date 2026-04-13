class ValidInputException(Exception):
   pass

class listElementAccess:
   def checkAccess(self,list1,index):
      count=0
      for i,value in enumerate(list1):
        count=i+count
        if value.isdigit():
           print("valid")
        else:
           raise ValidInputException("Error: Invalid input")
        if count!=(index+1):
           raise ValidInputException("Error: Index out of range")

l=listElementAccess()
nums=input("enter list:")
ind=int(input("enter index:"))

nums_array=nums.split(" ")

try:
   l.checkAccess(nums,ind)
except ValidInputException as e:
   print(e)

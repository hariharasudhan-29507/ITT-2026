# Author - Hariharasudhan A
class ValidInputException(Exception): # user defined exception
   pass

class listElementAccess:
   '''
   access the element in a list 
   if the element is not "int" then raise exception
   if the index is mismatching then raise exception
   '''
   def checkAccess(self,list1,index):
      count=0
      for i,value in enumerate(list1): # enumerate can be used to access elements along with position
        count=i+count
        if value.isdigit():
           print("valid")
        else:
           raise ValidInputException("Error: Invalid input") # user defined exception 1 for data type mismatching
        if count!=(index+1):
           raise ValidInputException("Error: Index out of range") # user defined exception 2 for index mismatching

l=listElementAccess()
nums=input("enter list:")
ind=int(input("enter index:"))

nums_array=nums.split(" ")

try: # try block
   l.checkAccess(nums,ind)
except ValidInputException as e: # catch 
   print(e)

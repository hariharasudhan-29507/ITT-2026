# Author - Hariharasudhan A
class safeDivision:
   '''
   simple exception throw cases on basic arithmetic division
   '''
   def divide(self,num1,num2):
      try:# try block
        div=num1/num2
        return div
      except ValueError: # catch 1
         print("Error: Not a Number")
      except ZeroDivisionError: # catch 2
         print("Error: Division by zero")

s=safeDivision()
numbers=input("enter numbers:")

# get input as string and parse them and feed them in input as int
nums=numbers.split(" ")

value=s.divide(int(nums[0]),int(nums[1]))
if value is not None:
   print("valid")

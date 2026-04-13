class safeDivision:
   def divide(self,num1,num2):
      try:
        div=num1/num2
        return div
      except ValueError:
         print("Error: Not a Number")
      except ZeroDivisionError:
         print("Error: Division by zero")

s=safeDivision()
numbers=input("enter numbers:")

nums=numbers.split(" ")

value=s.divide(int(nums[0]),int(nums[1]))
if value is not None:
   print("valid")

# Author - Hariharasudhan A
class LargeNum:
  '''
  simple largest among three numbers
  '''
  def isLarge(self,a,b,c): # ternary condition 
    print("number 1 is largest") if a>b and a>c else print("number 2 is largest") if b>c else print("number 3 is largest")
# object creation
l=LargeNum()
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
# function calling
l.isLarge(a,b,c)

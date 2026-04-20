# Author - Hariharasudhan A
class countEven:
  '''
  simple counting even numbers within the limit
  '''
  def count(self,n):
    count=0 # count variable
    if 1<=n<=100000:
      for i in range (1,n+1):
        if i%2==0: # even criterion
          count+=1 # counter
      print("count of even numbers:",count)
    else:
      print("enter a number within range(1-100000)")
# object declaration
c=countEven()
n=int(input("enter a number for limit:"))
# function calling
c.count(n)

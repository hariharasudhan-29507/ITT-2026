class countEven:
  def count(self,n):
    count=0
    if 1<=n<=100000:
      for i in range (1,n+1):
        if i%2==0:
          count+=1
      print("count of even numbers:",count)
    else:
      print("enter a number within range(1-100000)")
c=countEven()
n=int(input("enter a number for limit:"))
c.count(n)

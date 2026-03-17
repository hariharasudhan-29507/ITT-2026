class arryaColor:
  def color(self,arr):
    arr.sort()
    for i in range(len(arr)):
      if arr[i]==0:
        print("red",end=" ")
      elif arr[i]==1:
        print("blue",end=" ")
      elif arr[i]==2:
        print("green",end=" ")
      else:
        print("\nthe code has other than 0,1,2")
        break
a=arrayColor()
arr=eval(input("enter array of give color code:"))
a.color(arr)

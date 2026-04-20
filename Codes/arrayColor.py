# Author - Hariharasudhan A
class arrayColor:
  '''
  pair matching colors to code ,positive integer array 
  '''
  def color(self,arr):
    arr.sort() 
    '''
    sorting because the code is only 0,1,2 
    they will be at the start of the array if sorted having the numbers greater than 0,1,2 
    '''
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

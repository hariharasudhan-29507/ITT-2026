# Author - Hariharasudhan A
class remRep:
  '''
  remove target and replace it with place holder
  '''
  def Function(self,nums,val):
    l=len(nums)
    k=0
    print("[",end="")
    for i in range(0,l):
      if nums[i]!=val: # only elements that are not target
        k=k+1
        print(nums[i],",",end="")
    for i in range (0,l-k):
        print("_",",",end="") # place holders
    print("]",end="")
r=remRep()
nums=eval(input("enter list:"))
val=int(input("enter value to remove"))
r.Funtion(nums,val)

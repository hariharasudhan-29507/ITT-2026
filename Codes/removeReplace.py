class remRep:
  def Function(self,nums,val):
    l=len(nums)
    k=0
    print("[",end="")
    for i in range(0,l):
      if nums[i]!=val:
        k=k+1
        print(nums[i],",",end="")
    for i in range (0,l-k):
        print("_",",",end="")
    print("]",end="")
r=remRep()
nums=eval(input("enter list:"))
val=int(input("enter value to remove"))
r.Funtion(nums,val)

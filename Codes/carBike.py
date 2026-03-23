print("Ravi's shop")
prb=0
tyre_count=int(input("Enter number of tyres:"))
if  2<= tyre_count <= 100:
   if tyre_count%2==0:
      if tyre_count%4==0:
         prb=0
      else:
         prb=1
print("Will Ravi's friend be able to buy a bike ?")
if prb==1:
   print("YES")
else:
   print("NO")

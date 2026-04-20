# Author - Hariharasudhan A
class coinGame:
   def coin(self,A,B):
      if A>=B:
         return 1
      else:
         return 0
   def change(self,A,B):
      B=A+B
      return B

c=coinGame()
'''
coin swap occurs with every loser of the game // done using change() method
'''
suresh=int(input("enter number of coins for suresh:"))
sundar=int(input("enter number of coins for sundar:"))
#if coin returns 1 that means A is the winner ,0 B is the winner
winner=c.coin(suresh,sundar)
raja=int(input("enter number of coins for raja:"))

# match result 
if winner==1:
   print("N")
   sundar=c.change(raja,sundar)
   winner=c.coin(suresh,sundar)
else:
   print("S")
   suresh=c.change(raja,suresh)
   winner=c.coin(suresh,sundar)

if winner==1:
   print("N")
   sundar=c.change(suresh,sundar)
   winner=c.coin(suresh,sundar)
   if winner==1:
      print("N")
   else:
      print("S")
else:
   print("S")
   suresh=c.change(sundar,suresh)
   winner=c.coin(suresh,sundar)
   if winner==1:
      print("N")
   else:
      print("S")

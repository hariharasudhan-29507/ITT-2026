class Arith:
  def Arith(self,num1,num2,choice):
    match choice:
    case 1:
       print("sum :",num1+num2)
    case 2:
       print("difference :",num1-num2)
    case 3:
       print("multiplication :",num1*num2)
    case 4:
       print("division :",num1/num2)
    case 5:
       print("modulus :",num1%num2)
    case _ :
      print("enter a valid operation")
  
a=Arith()
num1=int(input("enter 1st number :"))
num2=int(input("enter 2nd number :"))
print("menu \n 1.addition(+)\n 2.subtraction(-)\n 3.multiplication(*)\n 4.division(/)\n 5.modulus(%)\n")
ch=int(input("enter choice for operation:"))
a.Arith(num1,num2,ch)

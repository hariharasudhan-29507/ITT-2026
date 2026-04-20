# Author - Hariharasudhan A
class Arith:
  '''
  simple menu based arithmetic operation 
  '''
  def Arith(self,num1,num2,choice):
    match choice: 
    case 1: # addition
       print("sum :",num1+num2)
    case 2: # subtraction
       print("difference :",num1-num2)
    case 3: # multiplication
       print("multiplication :",num1*num2)
    case 4: # division
       print("division :",num1/num2)
    case 5: # modulus
       print("modulus :",num1%num2)
    case _ : # default if other cases are not met
      print("enter a valid operation")
  
# object declaration
a=Arith()
num1=int(input("enter 1st number :"))
num2=int(input("enter 2nd number :"))
print("menu \n 1.addition(+)\n 2.subtraction(-)\n 3.multiplication(*)\n 4.division(/)\n 5.modulus(%)\n")
ch=int(input("enter choice for operation:"))
# function calling
a.Arith(num1,num2,ch)

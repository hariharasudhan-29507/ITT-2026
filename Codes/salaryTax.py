# Author - Hariharasudhan A 
class checkSalary:
  '''
  simple salary computation program using condition statement
  '''
  def checkTax(self,salary):
    # ternary condition
    print("no tax") if salary<=250000 else print("tax amount:",salary*0.005) if 250000<salary<500000 else print("tax amount:",salary*0.1) if 500000<salary<1000000 else print("tax amount:",salary*0.15)
c=checkSalary()
salary=int(input("enter salary:"))
c.checkTax(salary)

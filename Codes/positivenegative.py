# Author - Hariharasudhan
class posneg:
  '''
  simple positive or negative or zero finder 
  '''
  def isPNZ(def,num):
    # ternary condition
    res="number is positive"if num>0 else "number is negative" if num<0 else "number is zero"
    return res
p=posneg()
num=int(input("enter number:"))
res=p.isPNZ(num)
print(res)

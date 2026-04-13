class store:
  def Bill(self,amount):
    if amount>=5000:
      d_amount=amount*0.02
      amount-=d_amount
    elif 5000>=amount>=3000:
      d_amount=amount*0.01
      amount-=d_amount
    else:
      print("enter valid amount")
s=store()
amount=int(input("enter the purchase amount:"))
Total_amount=s.Bill(amount)
print("bill amount",Total_amount)

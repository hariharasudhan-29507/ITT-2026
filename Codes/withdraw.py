class Bank:
  def Withdraw(self,balance):
    if balance>=500:
      amount=int(input("enter amount to withdraw:"))
      if balance>amount and balance>0 and amount>0:
        if amount%100==0:
          balance=balance-amount
          print("withdrawed\nnew balance:",balance)
        else:
          print("cannot withdraw, not a multiple of 100")
        else:
          print("cannot withdraw, invalid balance")
      else:
        print("minimum balance should be 500")
b=Bank()
balance=int(input("enter the balance(minimum val must be 500):"))
b.Withdraw(balance)

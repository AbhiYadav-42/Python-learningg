# Create Account class with 2 attributes - balanace & account no.
# Create methods for debit , credit & printing the balance


class Account:
  def __init__(self,bal,acc_no):
    self.Balance = bal
    self.Account_No = acc_no
  
  def Debit(self, amount):
    self.Balance -= amount
    print(f"Rs.{amount} was debited from your Account")

  def Credit(self, amount):
    self.Balance += amount
    print(f"Rs.{amount} was credited from your Account")
    
  def Show_bal(self):
    return print(f"Balance: Rs.{self.Balance}")
  



# us1 = Account(100000 , 2456)
# print(f" Account number is #{us1.Account_No} \n And the Balance: Rs.{us1.Balance} " )

# us1.Debit(5000)

# us1.Credit(4)

# us1.Show_bal()

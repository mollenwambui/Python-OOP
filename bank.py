class Bank:
    def __init__(self,name,number,bankname) :
        self.name=name
        self.number=number
        self.balance=0
        self.bankname=bankname
        self.deposits=[]
        self.withdrawals=[]


      

    def deposit(self,amount):
        if amount<=0:
            return f"Deposit should be greater than 0"
        else:
          self.balance+=amount
          self.deposits.append(amount)
        return f"Hello  you have sucessfully deposited {amount} your current balance is {self.balance} "

    def  withdraw(self,amount) :
        if amount<=self.balance and amount>0:
          transactions=amount+100
          self.balance-=transactions
          self.withdrawals.append(amount)
        else:
            return "withdrawal failed"  
        return f"Hello you have withdrawn {amount}current balance is {self.balance}"

    def deposit_statements(self):
         for x in self.deposits:
             print(f"Hello you have deposited {x} ",end="\n")
             
        

    def withdrawals_statement(self):
         for x in self.withdrawals:
             print(f"Hello you have withdrawn {x} ",end="\n")
   

    def current_balance(self):
        return f"Hello your current balance is  {self.balance} "



             
from datetime import datetime
from time import strftime



class Bank:
    def __init__(self,name,number,bankname) :
        self.name=name
        self.number=number
        self.balance=0
        self.bankname=bankname
        self.deposits=[]
        self.my_balance=0
        self.withdrawals=[]
        self.loan_balance=0
      


      

    def deposit(self,amount):
        if amount<=0:
            return f"Deposit should be greater than 0"
        else:
          self.balance+=amount
          self.deposits.append(amount)
          details={'date':strftime("%d/%m/%y :%H:%M:%S"),'amount':{amount},'narration':f"deposits"}
          print (details)
        return f"Hello  you have sucessfully deposited {amount} your current balance is {self.balance} "

    def  withdraw(self,amount) :
        self.transaction=100
        if amount<=self.balance +self.transaction and amount>0:
          transactions=amount+self.transaction
          self.balance-=transactions
          details={'date':strftime("%d/%m/%y"),'amount':{amount},'naration':f"withdrawal"}
          print (details)
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

    def full_statement(self) :
         for x,y in self.deposits,self.withdrawals :
            time= strftime("%H:%M:%S") 
            print(f"{time}  deposits {x}")
            print(f"{time}  withdraw {y}")
            

    def borrowing(self,loan):
        self.loan=loan
        sum=0
        for x in self.deposits:
            sum+=x
        intrest=loan*(3/100)  
        total_amount=self.loan+intrest
        self.total_amount=total_amount
        if len(self.deposits )>10 and self.loan>100 and self.loan<=1/3*(sum)  and self.my_balance==0 and self.loan_balance==0:
            return f"Hello {self.name}  you have successfully  received {self.loan} loan with a 3% intrest and you will return {self.total_amount}"
        else:
            return f"Operation unsuccessfull!"    

             

    def loan_repayment(self,pay):
        self.loan_balance+=self.total_amount
        self.loan_balance-=pay
        print(f"Hello {self.name} you have paid {pay}  your  current loan balance is {self.loan_balance} ")
        overpaid=pay-self.total_amount
        if pay>self.loan:
            self.deposits+=overpaid

    def transfer(self,amount,account) :
        self.amount=amount
        self.account=account    
        if self.amount<self.balance:
            self.account+=self.amount
            self.balance-=self.amount
        print(f"You have successfully sent {self.amount} to {self.account} your current balance is {self.balance}")   
        

        
               
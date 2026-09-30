
class Bank_acount :
    def __init__(self , name , acc_holder,balance) :
        self.name = name
        self.acc_holder = acc_holder
        self.balance= balance

    def deposite(self,amount) :
       if amount > 0:
          self.balance += amount
          print(f"{amount},deposite succesfully")
       else :
          print("invalid amount")  

    def withdraw (self , amount)  :
       if amount < 0:
          print("inavalid withdraw amount")
       elif amount > self.balance:
            print("Insufficient Balance!")
       else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")   

    def check_balance (self):
         print(f"Account Holder : {self.acc_holder}")
         print(f"Current Balance: {self.balance}")
         print("-" * 30)


       

    
acc1= Bank_acount( "ali" , 1234 ,10000)
acc1.deposite(3000)
acc1.withdraw(2000)
acc1.check_balance()


employees = {
    "101" :develpors1,
    "102" :develpors2,
    "103" :manager1,
    "104" :manager2,
}
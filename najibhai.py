from abc import ABC , abstractmethod
class Membership (ABC):
    def __init__(self , prize_per_month):
        if prize_per_month <=0 :
            raise ValueError("prize must be greater than zero")
        self.__prize_per_month =  prize_per_month

    def get_month (self) :
        return self.__prize_per_month

    @abstractmethod
    def calculate_fee (self , month):
        pass
class  BasicMembership (Membership) :
    def __init__(self):
        super().__init__(2000)
    def calculate_fee (self , month):
        return self.get_month() * month

class PremiumMembership (Membership):
    def __init__(self):
        super().__init__(3500)  
    def calculate_fee (self , month):
            return self.get_month() * month

class VIPMembership (Membership) :
    def __init__(self):
            super().__init__(5000)  
    def calculate_fee (self , month):
        return self.get_month() * month + 2000

BasicMembership1 =  BasicMembership ()
PremiumMembership1 = PremiumMembership()
VIPMembership1 = VIPMembership()


Memberships ={}

Memberships["moo1"]=BasicMembership1
Memberships["pee1"]=PremiumMembership1
Memberships["vee1"]=VIPMembership1

Membershipe ={
     "moo1" : BasicMembership1,
     "pee1" : PremiumMembership1,
     "vee1" : VIPMembership1,
}
acc_membership ={}

print("\n show available membership")
for acc_Membership in Memberships.items():
    if acc_Membership not in Memberships:
        print (acc_Membership,"-" , type(Memberships).__name__)

member_id = (input("enter the member_id:"))
customer = input("enter the name")       


if customer in Memberships.values():
    print("Customer already has a membership member")

else :
         
         month= int(input("enter a month"))
         total_payment = Memberships[member_id].calculate_fee(month)
         
         print("Total Rent:", total_payment)
             
         print("\nRented Vehicles:")
         for member_id, customer in Memberships.items():
             print(member_id, "->", customer)
        
 

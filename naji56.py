from abc import ABC , abstractmethod

class vehicle (ABC):
    def __init__(self , prize_per_day):
        if  prize_per_day <= 0:
            raise ValueError("prize mus be greater than zero")
        self.__prize_per_day = prize_per_day   

    def get_prize(self):
        return self.__prize_per_day

    @abstractmethod
    def calculate_rent(self,days) :
        return
class car (vehicle):
    def __init__(self):
        super().__init__(5000)
    def calculate_rent(self,days) :
        return self.get_prize() * days
class bike (vehicle):
    def __init__(self):
        super().__init__(2000)
    def calculate_rent(self,days) :
        return self.get_prize() * days 
class van (vehicle):
    def __init__(self):
        super().__init__(8000)
    def calculate_rent(self,days) :
        return (self.get_prize() * days + 2000) 

car1 = car()
bike1 = bike()
van1 = van()

vehicles= {}

vehicles["LEA-123"] = car1
vehicles["LEB-456"] = bike1
vehicles["LEC-789"] = van1

vehicles = {
    "LEA-123": car1,
    "LEB-456": bike1,
    "LEC-789": van1
}

rented = {}

print("\n show available vehicle")
for plate, vehicle in vehicles.items():
    if plate not in rented:
        print (plate ,"-" , type(vehicles).__name__)

plate = input("enter tha plate no:")
costumer =input("enter the name")

if costumer in rented.values():
    print("Customer already has a rented vehicle")
elif plate in rented :
    print("vehicle is already rented")
elif plate not in vehicle:
    print("vehicle not found")
else :
    rented[plate] = costumer
    days= int(input("enter a days"))
    total_rent = vehicle[plate].calculate_rent(days)
    
    print("Total Rent:", total_rent)
        
    print("\nRented Vehicles:")
    for plate, customer in rented.items():
        print(plate, "->", customer)
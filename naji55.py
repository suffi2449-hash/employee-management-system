from abc import ABC , abstractmethod

class vehicles (ABC):
    def __init__(self , prize_per_day):
        if prize_per_day <= 0:
            raise ValueError ("Price must be greater than zero")
        self.__prize_per_day = prize_per_day

    def get_prize (self):
      return self.__prize_per_day

    @abstractmethod
    def calculate_rent (self ,days):
            pass

class car (vehicles):
    def __init__(self):
        super().__init__(5000)
    def calculate_rent (self ,days):
        return self.get_prize() * days

class bike (vehicles):
    def __init__(self):
        super().__init__(1500)
    def calculate_rent (self ,days):
        return self.get_prize() * days


class van (vehicles):
    def __init__(self):
        super().__init__(8000)
    def calculate_rent (self ,days):
        return (self.get_prize() * days +2000)
    

car1 = car()        
bike1 = bike()
van1 = van()

vehicle = {}

vehicle["LEA-123"] = car1
vehicle["LEB-456"] = bike1
vehicle["LEC-789"] = van1

vehicle = {
    "LEA-123": car1,
    "LEB-456": bike1,
    "LEC-789": van1
}

rented = {}

print ("available vehicle:")
for plate ,vehicles in vehicle.items():
    if plate not in rented:
        print(plate, "-", type(vehicle).__name__)

plate = input ("enter plate number:")
customer =input("enter customer name:")

if customer in rented.values():
    print("Customer already has a rented vehicle")
elif plate in rented :
    print("vehicle is already rented")
elif plate not in vehicle:
    print("vehicle not found")
else :
    rented [plate] = customer
       
    days = int(input("Enter Number of Days: "))
    total_rent = vehicle[plate].calculate_rent(days)

    print("Total Rent:", total_rent)
    
print("\nRented Vehicles:")
for plate, customer in rented.items():
    print(plate, "->", customer)
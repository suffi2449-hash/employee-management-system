from abc import ABC ,abstractmethod

class vehicles (ABC):
    def __init__(self , prize_per_days):
        if prize_per_days<=0:
            raise ValueError ("prize must be greater than zero")
        self.__prize_per_days= prize_per_days

    def get_prize (self):
        return self.__prize_per_days

    @abstractmethod
    def calculate_rent(self , days):
        pass

class car (vehicles):
    def __init__(self):
        super().__init__(5000)
    def calculate_rent(self , days):
        return self.get_prize * days 

class bike (vehicles) :
        def __init__(self):
         
         super().__init__(2000)
        def calculate_rent(self , days):
            return self.get_prize * days 

class van (vehicles) :
        def __init__(self):
         
         super().__init__(8000)
        def calculate_rent(self , days):
            return self.get_prize * days + 2000

car1 = car()
bike1 = bike()        
van1 = van()        

vehicle = {}


vehicle["LEA-123"] = car1
vehicle["LEB-456"] = bike1
vehicle["LEC-789"] = van1

vehicle = {
    "LEB-ABD" : car1,
    "LEC-SDF" :bike1,
    "LER-THJ" : van1
}

rented = {}

print ("\n print available vehicle")
for plate,vehicles in vehicle.items():
    if plate not in rented :
        print(plate , "-" ,type(vehicle).__name__)

plate = int(input("enter the plate no:"))
costumer = input("enter the name")




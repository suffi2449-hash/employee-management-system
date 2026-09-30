from abc import ABC , abstractmethod

class  vehicle(ABC) :
    def __init__(self ,prize_per_day):
        if prize_per_day <= 0:
            raise ValueError ("Price must be greater than zero")
        self.__prize_per_day = prize_per_day

    def get_price(self):
        return self.__prize_per_day

    @abstractmethod
    def calculate_rent(self,days):
        pass
print("a")


class car (vehicle) :
    def __init__(self):
        super().__init__(5000)
    def calculate_rent (self , days):
        return self.get_prize() * days
            

class bike (vehicle):
      def __init__(self):
        super().__init__(1500)
      def calculate_rent(self, days):
        return self.get_price() * days
          


class van (vehicle) :
     def __init__(self):
        super().__init__(8000)
     def calculate_rent(self , days):
      return (self.get_price()*days +2000)
print("A")

car1 = car()
bike1= bike()
van1 = van()

vehicles = {}

vehicles["LEA-123"] = car1
vehicles["LEB-456"] = bike1
vehicles["LEC-789"] = van1

vehicles = {
    "LEA-123": car1,
    "LEB-456": bike1,
    "LEC-789": van1
}

# Store rented vehicles
rented = {}

# Show available vehicles
print("Available Vehicles:")
for plate, vehicle in vehicles.items():
    if plate not in rented:
        print(plate, "-", type(vehicle).__name__)

# Take input
plate = input("Enter Plate Number: ")
customer = input("Enter Customer Name: ")

# Check customer
if customer in rented.values():
    print("Customer already has a rented vehicle.")

# Check vehicle
elif plate in rented:
    print("Vehicle is already rented.")

elif plate not in vehicles:
    print("Vehicle not found.")

else:
    rented[plate] = customer

    days = int(input("Enter Number of Days: "))
    total_rent = vehicles[plate].calculate_rent(days)

    print("Total Rent:", total_rent)

# Show rented vehicles
print("\nRented Vehicles:")
for plate, customer in rented.items():
    print(plate, "->", customer)

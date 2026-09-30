from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    def __init__(self, price_per_day):
        if price_per_day <= 0:
            raise ValueError("Price must be greater than zero")

        self.__price_per_day = price_per_day

    def get_price(self):
        return self.__price_per_day

    @abstractmethod
    def calculate_rent(self, days):
        pass


# Car Class
class Car(Vehicle):

    def __init__(self):
        super().__init__(5000)

    def calculate_rent(self, days):
        return self.get_price() * days


# Bike Class
class Bike(Vehicle):

    def __init__(self):
        super().__init__(1500)

    def calculate_rent(self, days):
        return self.get_price() * days


# Van Class
class Van(Vehicle):

    def __init__(self):
        super().__init__(8000)

    def calculate_rent(self, days):
        return self.get_price() * days + 2000


# =========================
# Main Program
# =========================

# Objects
car1 = Car()
bike1 = Bike()
van1 = Van()

# Dictionary of all vehicles
vehicles = {
    "LEA-123": car1,
    "LEB-456": bike1,
    "LEC-789": van1
}

# Dictionary of rented vehicles
rented = {}

# Show available vehicles
print("\nAvailable Vehicles")
for plate, vehicle in vehicles.items():
    if plate not in rented:
        print(plate, "-", type(vehicle).__name__)

# Rent Vehicle
customer = input("\nEnter Customer Name: ")
plate = input("Enter Vehicle Plate Number: ")

# Customer can rent only one vehicle
if customer in rented.values():
    print("Customer already has a rented vehicle.")

# Vehicle already rented
elif plate in rented:
    print("Vehicle is already rented.")

# Plate not found
elif plate not in vehicles:
    print("Vehicle not found.")

# Rent vehicle
else:
    rented[plate] = customer

    days = int(input("Enter Number of Days: "))

    total = vehicles[plate].calculate_rent(days)

    print("\nVehicle Rented Successfully")
    print("Customer :", customer)
    print("Plate    :", plate)
    print("Total Rent:", total)

# Show Available Vehicles Again
print("\nAvailable Vehicles")
for plate, vehicle in vehicles.items():
    if plate not in rented:
        print(plate, "-", type(vehicle).__name__)

# Show Rented Vehicles
print("\nRented Vehicles")
for plate, customer in rented.items():
    print(plate, "->", customer)
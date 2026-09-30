
from abc import ABC , abstractmethod

class employee (ABC):
    def __init__ (self ,name ,employee_id, per_month_salery):
        if per_month_salery <= 0:
            raise ValueError ("prize mus be greater then zero")
        self.__per_month_salery = per_month_salery
        self.employee_info={
            "name" :name,
            "employee_id":employee_id
        }
    def get_salery (self):
        return  self.__per_month_salery 
    def get_details(self):
        return self.employee_info
    @abstractmethod
    def calculate_salery(self ,month):
        return

class devolper (employee) :
    def __init__(self,name ,employee_id ):
        super().__init__(name ,employee_id ,25000)
    def calculate_salery (self , month):
        return self.get_salery() * month

class manager (employee):
    def __init__(self,name ,employee_id,):
        super().__init__(name ,employee_id, 30000)    
    def calculate_salery (self , month):
        return self.get_salery()* month

develpors1 = devolper("sufyan",101,)    
develpors2 = devolper("ali",102,)

manager1 = manager("talha" ,103,)
manager2 = manager("naji",104,)

employees ={}

employees[101] = develpors1
employees[102] = develpors2
employees[103] = manager1
employees[104] = manager2



while True :
     print("\n===== Employee Management System =====")
    
     print("1. Employees")
     print("2. Salary")
     print("3. Exit")

     choice = input ("enter choice :")
     if choice == "1":
      for emp in employees.values():
        print(emp.get_details())
     elif choice == "2" :
            month = int(input("Enter Months: "))

            for emp in employees.values():
             print(emp.get_details())
             print("Salary:", emp.calculate_salery(month))
             
     elif choice == "3":
     
        print("Program Closed")  
        break
     

     else :
      print("invalid")
      


       
    
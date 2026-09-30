class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("\n--------------------------")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("--------------------------")

    def increase_salary(self, amount):

        if amount > 0:
            self.salary += amount
            print("Salary Increased Successfully!")

        else:
            print("Invalid Amount!")

    def check_salary(self):
        print("Current Salary :", self.salary)


employees = []

try:

    total = int(input("How many employees do you want to add? : "))

    for i in range(total):

        print(f"\nEnter Details of Employee {i+1}")

        emp_id = int(input("Enter Employee ID : "))
        name = input("Enter Employee Name : ")
        salary = float(input("Enter Employee Salary : "))

        employee = Employee(emp_id, name, salary)

        employees.append(employee)

    print("\nEmployees Added Successfully!")

except:

    print("Invalid Input!")


def show_employee():

    if len(employees) == 0:

        print("No Employee Found")

    else:

        for emp in employees:
            emp.display()


def increase():

    try:

        emp_id = int(input("Enter Employee ID : "))

        for emp in employees:

            if emp.emp_id == emp_id:

                amount = float(input("Enter Increase Amount : "))

                emp.increase_salary(amount)

                return

        print("Employee Not Found")

    except:

        print("Invalid Input")


def check():

    try:

        emp_id = int(input("Enter Employee ID : "))

        for emp in employees:

            if emp.emp_id == emp_id:

                emp.check_salary()

                return

        print("Employee Not Found")

    except:

        print("Invalid Input")


while True:

    print("\n===== Employee Management System =====")

    print("1. Show Employees")
    print("2. Increase Salary")
    print("3. Check Salary")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        show_employee()

    elif choice == "2":

        increase()

    elif choice == "3":

        check()

    elif choice == "4":

        print("Program Closed")

        break

    else:

        print("Invalid Choice")
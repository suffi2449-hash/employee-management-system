class Student:

    def __init__(self, name, roll, age, marks):
        self.name = name
        self.roll = roll
        self.age = age
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("\n---------------------------")
        print("Name  :", self.name)
        print("Roll  :", self.roll)
        print("Age   :", self.age)
        print("Marks :", self.marks)
        print("Grade :", self.get_grade())
        print("---------------------------")


students = []


def add_student():
    try:
        name = input("Enter Name : ")
        roll = int(input("Enter Roll Number : "))
        age = int(input("Enter Age : "))
        marks = float(input("Enter Marks : "))

        student = Student(name, roll, age, marks)

        students.append(student)

        print("\nStudent Added Successfully!")

    except:
        print("\nInvalid Input!")


def show_students():

    if len(students) == 0:
        print("\nNo Students Found!")
        return

    for student in students:
        student.display()


while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("\nProgram Closed.")
        break

    else:
        print("\nInvalid Choice!")




class student :
    def __init__(self ,name , roll , age , masrks):
        self.name = name
        self.roll = roll
        self.age = age
        self.marks = masrks

    def get_grade (self):
        if self.marks   >= 90 :
            return "A+"
        elif self.marks >= 80 :
            return "A"
        elif self.marks >= 70 :
            return "B"
        elif self.marks >= 60 :
            return "C"
        elif self.marks >= 50 :
            return "D"
        else :
            return "fail"

    print("a")    

    def display(self):

        print("\n---------------------------")
        print("Name  :", self.name)
        print("Roll  :", self.roll)
        print("Age   :", self.age)
        print("Marks :", self.marks)
        print("Grade :", self.get_grade())
        print("---------------------------")

student = []

def add_student ():
    try:
        name = input("enter the name: ")
        roll_no = int(input("enter the roll no :"))
        age  = int (input("enter the age :")) 
        marks = int (input("enter the marks")) 

        
        student = Student(name, roll, age, marks)

        students.append(student)

        print("\nStudent Added Successfully!")

    except:
        print("\nInvalid Input!")


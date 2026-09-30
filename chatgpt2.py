class Student:

    def __init__(self, student_id, name, marks):

        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):

        print("\n----------------------------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Marks      :", self.marks)
        print("----------------------------")

    def update_marks(self, new_marks):

        if new_marks >= 0:

            self.marks = new_marks
            print("Marks Updated Successfully!")

        else:

            print("Invalid Marks!")

    def check_marks(self):

        print("Current Marks :", self.marks)


students = []

try:

    total = int(input("How many students do you want to add? : "))

    for i in range(total):

        print(f"\nEnter Details of Student {i+1}")

        student_id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        marks = float(input("Enter Student Marks : "))

        student = Student(student_id, name, marks)

        students.append(student)

    print("\nStudents Added Successfully!")

except:

    print("Invalid Input")


def show_students():

    if len(students) == 0:

        print("No Student Found")

    else:

        for stu in students:

            stu.display()

def search_student():
    try:

        student_id = int(input("Enter Student ID : "))

        for stu in students:

            if stu.student_id == student_id:

                print("\nStudent Found!")
                stu.display()
                return

        print("Student Not Found")
    
    except:

        print("Invalid Input")

def update_student_marks():

    try:

        student_id = int(input("Enter Student ID : "))

        for stu in students:

            if stu.student_id == student_id:

                new_marks = float(input("Enter New Marks : "))

                stu.update_marks(new_marks)

                return

        print("Student Not Found")

    except:

        print("Invalid Input")

def check_student_marks():

    try:

        student_id = int(input("Enter Student ID : "))

        for stu in students:

            if stu.student_id == student_id:

                stu.check_marks()

                return

        print("Student Not Found")

    except:

        print("Invalid Input")


def check_student_marks():

    try:

        student_id = int(input("Enter Student ID : "))

        for stu in students:

            if stu.student_id == student_id:

                stu.check_marks()

                return

        print("Student Not Found")

    except:

        print("Invalid Input")


while True:

    print("\n====== Student Management System ======")
    print("1. Show Students")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Check Marks")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        show_students()

    elif choice == "2":

        search_student()

    elif choice == "3":

        update_student_marks()

    elif choice == "4":

        check_student_marks()

    elif choice == "5":

        print("Program Closed")
        break

    else:

        print("Invalid Choice")
# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
1
    def display_info(self):
        print(f"\n--- Person Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Student subclass
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print("Role: Student")
        print("-" * 30)

# Lecturer subclass
class Lecturer(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print("Role: Lecturer")
        print("-" * 30)

# Staff subclass
class Staff(Person):
    def __init__(self, name, age, gender, staff_id, role):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Role/Position: {self.role}")
        print("Role: Administrative Staff")
        print("-" * 30)

# Function to collect input and create objects
def create_person():
    print("Select Person Type:")
    print("1. Student")
    print("2. Lecturer")
    print("3. Staff")
    choice = input("Enter choice (1/2/3): ")

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")

    if choice == '1':
        student_id = input("Enter Student ID: ")
        course = input("Enter Course: ")
        person = Student(name, age, gender, student_id, course)

    elif choice == '2':
        employee_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")
        person = Lecturer(name, age, gender, employee_id, department)

    elif choice == '3':
        staff_id = input("Enter Staff ID: ")
        role = input("Enter Staff Role: ")
        person = Staff(name, age, gender, staff_id, role)

    else:
        print("Invalid choice.")
        return

    person.display_info()

# Run the program
create_person()

# =========================================
# Name: Kwadwo Owusu
# ID: kwaowu7442
# Date: 2026
# Project: Week 1 - Student Management System
# =========================================

# Base Class (Inheritance)
class Person:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

# Composition Class
class Address:
    def __init__(self, country):
        self.country = country

# Derived Class (Inheritance + Composition)
class Student(Person):
    def __init__(self, name, student_id, course, address):
        super().__init__(name, student_id)  # Inheritance
        self.course = course
        self.address = address  # Composition

    def display(self):
        print(f"{self.student_id} | {self.name} | {self.course} | {self.address.country}")


# Main Output
print("========================================")
print(" PROJECT WEEK 1: STUDENT MANAGER")
print(" Name: Kwadwo Owusu")
print(" ID: kwaowu7442")
print("========================================\n")

print("Welcome! This application manages student records.\n")

# Creating object (realistic info)
addr = Address("USA")
student = Student(
    "Kwadwo Owusu",
    "kwaowu7442",
    "Advanced Object-Oriented Programming using C#",
    addr
)

# Display
print("ID | Name | Course | Location")
print("--------------------------------------------------------------")
student.display()

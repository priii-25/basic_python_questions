                                          #Practical No 3:Conditional Statements
#Q1)
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
 print(num, " is divisible by 3 and 5 both.")
else:
 print(num, " is not divisible by 3 and 5 both.")
#Q2)
num = int(input("Enter a number: "))
if num % 5 == 0:
 print(num, " is a multiple of 5.")
else:
 print(num, " is not a multiple of 5.")
#Q3)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
 print(a, " is the greatest number.")
elif b > a:
 print(b, " is the greatest number.")
else:
 print("Numbers are equal.")
#Q4)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
 print(a, " is the greatest number.")
elif b > a and b > c:
 print(b, " is the greatest number.")
elif c > a and c > b:
 print(c, " is the greatest number.")
else:
 print("No two values are the same.")
#Q5)
import math
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
 root1 = (-b + math.sqrt(discriminant)) / (2 * a)
 root2 = (-b - math.sqrt(discriminant)) / (2 * a)
 print("The roots are real and distinct.")
 print("Root 1 is: ", root1)
 print("Root 2 is: ", root2)
elif discriminant == 0:
 root = -b / (2 * a)
 print("The roots are real and equal.")
 print("Root is: ", root)
else:
 real_part = -b / (2 * a)
 imaginary_part = math.sqrt(-discriminant) / (2 * a)
 print("The roots are imaginary.")
 print("Root 1 is: ", real_part, "+", imaginary_part, "i")
 print("Root 2 is: ", real_part, "-", imaginary_part, "i")
#Q6)
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 print(year, " is a leap year.")
else:
 print(year, " is not a leap year.")
#Q7)
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 leap_year = True
else:
 leap_year = False
if month == 2:
 if leap_year:
 max_days = 29
 else:
 max_days = 28
#Q8)
name = input("Enter the name of the student: ")
roll_number = input("Enter the roll number of the student: ")
sapid = input("Enter the SAP ID of the student: ")
semester = input("Enter the semester of the student: ")
course = input("Enter the course of the student: ")
subject_marks = {}
for i in range(5):
 subject_name = input(f"Enter the name of subject {i+1}: ")
 subject_marks[subject_name] = int(input(f"Enter the marks of subject {i+1}: "))
total_marks = sum(subject_marks.values())
percentage = (total_marks/500)*100
cgpa = percentage/10
if cgpa >= 9.1:
 grade = "O (Outstanding)"
elif cgpa >= 8.1:
 grade = "A+"
elif cgpa >= 7.1:
 grade = "A"
elif cgpa >= 6.1:
 grade = "B+"
elif cgpa >= 5.1:
 grade = "B"
elif cgpa >= 3.5:
 grade = "C+"
else:
 grade = "F"
print("\n\nGrade Sheet")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"SAP ID: {sapid}")
print(f"Semester: {semester}")
print(f"Course: {course}")
print("Subject Name: Marks")
for subject, marks in subject_marks.items():
 print(f"{subject}: {marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.1f}")
print(f"Grade: {grade}")

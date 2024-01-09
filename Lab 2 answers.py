                                   #Practical No 2:Use of input statements, operators
#Q1)
x = 9
y = 7
addition = x + y
multiplication = x * y
division = x / y
subtraction = x - y
print("Addition: ", addition)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Subtraction: ", subtraction)
#Q2)
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius**2)
print("Area of the circle is: ", area)
#Q3)
x = 4
y = 3
result = (x+y) ** 2
print(result)
#Q4)
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(a**2 + b**2)
print("Length of the hypotenuse is: ", c)
#Q5)
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple interest is: ", simple_interest)
#Q6)
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)
#Q7)
seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print("Time is: ", hours, " hours, ", minutes, " minutes, and ", seconds, " seconds.")
#Q8)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping, a = ", a, " and b = ", b)
#Q9)
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n+1):
 sum += i
print("Sum of first ", n, " natural numbers is: ", sum)
#Q10)
# Bitwise AND
print("Bitwise AND Truth Table:")
print("a\tb\ta & b")
print("--------------")
for a in [0, 1]:
 for b in [0, 1]:
 print(a, "\t", b, "\t", a & b)
# Bitwise OR
print("\n Bitwise OR Truth Table:")
print("a\tb\ta | b")
print("--------------")
for a in [0, 1]:
 for b in [0, 1]:
 print(a, "\t", b, "\t", a | b)
# Bitwise XOR
print("\n Bitwise XOR Truth Table:")
print("a\tb\ta ^ b")
print("--------------")
for a in [0, 1]:
 for b in [0, 1]:
 print(a, "\t", b, "\t", a ^ b)
#Q11)
num = int(input("Enter a number: "))
n = int(input("Enter the number of bits to shift: "))
left_shift = num << n
right_shift = num >> n
print("Left shift value is: ", left_shift)
print("Right shift value is: ", right_shift)
#Q12)
seq = [10, 20, 56, 78, 89]
num = int(input("Enter a number to search: "))
if num in seq:
 print(num, " is present in the sequence.")
else:
 print(num, " is not present in the sequence.")
#Q13)
string = input("Enter a string: ")
char = input("Enter a character to search: ")
if char in string:
 print(char, " is present in the string.")
else:
 print(char, " is not present in the string.")

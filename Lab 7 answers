                                                    #Practical No 7:Functions
#Q1)
def find_max_min(numbers):
 max_num = numbers[0]
 min_num = numbers[0]
 for num in numbers:
 if num > max_num:
 max_num = num
 elif num < min_num:
 min_num = num
 return max_num, min_num
#Q2)
def sum_of_cubes(n):
 if n == 0:
 return 0
 else:
 return (n-1)**3 + sum_of_cubes(n-1)
#Q3)
def print_numbers(n):
 if n == 1:
 print(1)
 else:
 print_numbers(n-1)
 print(n)
Q4)
def fibonacci(n):
 if n <= 1:
 return n
 else:
 return fibonacci(n-1) + fibonacci(n-2)
n = 10
for i in range(n):
 print(fibonacci(i))
#Q5)
volume_of_cone = lambda r, h: (1/3) * 3.14 * r**2 * h
#Q6)
max_min_tuple = lambda lst: (max(lst), min(lst))
#Q7)
# Keyword argument example
def greet(name, greeting):
 print(f"{greeting}, {name}!")
greet(name="Alice", greeting="Hello")
greet(greeting="Hi", name="Bob")
# Default argument example
def repeat(text, times=2):
 print(text * times)
repeat("hello")
repeat("world", 3)
# Variable length argument example
def sum_all(*numbers):
 result = 0
 for number in numbers:
 result += number
 return result
print(sum_all(1, 2, 3))
print(sum_all(4, 5, 6, 7, 8)) 

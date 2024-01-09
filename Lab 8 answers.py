                                     #Practical No 8:File handling and Exception Handling
#Q1) (A)
with open("name.txt", "r") as file:
 names = file.readlines()
 count = len(names)
 print("Total names:", count)
(B)
with open("name.txt", "r") as file:
 names = file.readlines()
 count = 0
 vowels = ['a', 'e', 'i', 'o', 'u']
 for name in names:
 if name[0].lower() in vowels:
 count += 1
 print("Names starting with vowel:", count)
(C)
with open("name.txt", "r") as file:
 names = file.readlines()
 longest_name = max(names, key=len).strip()
 print("Longest name:", longest_name)
#Q2)
numbers = [10, 20, 30, 40, 50]
with open("numbers.txt", "w") as file:
 for num in numbers:
 file.write(str(num) + "\n")
with open("numbers.txt", "r") as file:
 numbers = file.readlines()
 numbers = [int(num.strip()) for num in numbers]
max_num = max(numbers)
print("Max number:", max_num)
average = sum(numbers) / len(numbers)
print("Average of numbers:", average)
count = len([num for num in numbers if num > 100])
print("Numbers greater than 100:", count)
#Q3)
(A)
with open("city.txt", "r") as file:
 cities = file.readlines()
 print("City details:")
 for city in cities:
 city_data = city.split()
 name, population, area = city_data[0], float(city_data[1]), float(city_data[2])
 print(name, population, area)
(B)
 with open("city.txt", "r") as file:
 cities = file.readlines()
 print("Cities with population more than 10 Lakhs:")
 for city in cities:
 city_data = city.split()
 name, population, area = city_data[0], float(city_data[1]), float(city_data[2])
 if population > 10:
 print(name)
(C)
with open("city.txt", "r") as file:
 cities = file.readlines()
 area_sum = sum([float(city.split()[2]) for city in cities])
 print("Sum of areas of all cities:", area_sum)
#Q4)
n = int(input())
for i in range(n):
 try:
 a, b = input().split()
 print(int(a) // int(b))
 except ValueError:
 print("Error Code: invalid literal for int() with base 10:", a)
 except ZeroDivisionError:
 print("Error Code: integer division or modulo by zero")

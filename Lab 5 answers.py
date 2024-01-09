                                                  #Practical No 5:String and Sets
#Q1)
string = input("Enter a string: ")
count = 0
for char in string:
 if char.isupper():
 count += 1
print("Number of capital letters:", count)
#Q2)
string = input("Enter a string: ")
count = 0
vowels = "aeiouAEIOU"
for char in string:
 if char in vowels:
 count += 1
print("Total number of vowels:", count)
#Q3)
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
 print(word)
#Q4)
string = input("Enter a string: ")
substring = input("Enter a substring: ")
count = 0
for i in range(len(string)):
 if string[i:i+len(substring)] == substring:
 count += 1
print("Number of times substring occurs:", count)
#Q5)
string = input("Enter a string: ")
alphabets = "abcdefghijklmnopqrstuvwxyz"
counts = {}
for char in alphabets:
 counts[char] = string.lower().count(char)
print("Occurrences of each alphabet:", counts)
#Q6)
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
#Q7)
n = int(input("Enter the number of fruits in each set: "))
s1 = set()
s2 = set()
print("Enter fruits in set 1:")
for i in range(n):
 s1.add(input())
print("Enter fruits in set 2:")
for i in range(n):
 s2.add(input())
common_fruits = s1.intersection(s2)
print("Common fruits:", common_fruits) # part(a)
unique_fruits = s1.difference(s2)
print("Fruits only in set 1:", unique_fruits) #part(b)
all_fruits = s1.union(s2)
print("Count of all fruits:", len(all_fruits)) #part(c)
#Q8)
S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}
print("Intersection of S1 and S2:", S1.intersection(S2))
print("Union of S1 and S2:", S1.union(S2))
print("Difference of S1 and S2:", S1.difference(S2))
print("Difference of S2 and S1:", S2.difference(S1))
print("Symmetric difference of S1 and S2:", S1.symmetric_difference)

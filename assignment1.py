#Task1: Variable Manipulation

name = "Nazmun"
age =    37
print("My name is %s and I am %d years old." % (name,age))

#Task2: Data Types and Type Conversion


num1 = 10
num2 =10.5
num1_float = float(num1)
num2_int = int(num2)
print("num1 :", num1)
print("num1_float", num1_float)
print("num2 :", num2)
print("num2_int", num2_int)

#Task3: String Manipulation

sentence = "Python Programming Is Fun!"
print("Length of the string:", len(sentence))
print("8th character:",sentence[7])
substring = sentence[0:6]
result = substring + " I enjoy it!"
print(result)

#Task4: Lists and List Manipulation

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("grape")
fruits.remove("banana")
print("Length of the list is", len(fruits))
sliced_fruits =fruits[2:4]
extra_fruits = ["kiwi", "lemon"]
combined_list = sliced_fruits + extra_fruits
print("Combined List:", combined_list)

#Task5: Conditional Statement for even or odd Number
num = 10
mod = num % 2
if mod > 0:
   print("The number is odd",num)
else:
   print("The number is even", num)  

#Task6: Calculate the sum of numbers and print the result
i = 0
while (i <= 10) :
   print(i)
   i = i + 1
j = 0
sum = 0
while (j <= 10):
   sum = sum + j 
   j = j + 1
   print("The Sum of Numbers:", sum)

#Task7: Function

def calculate_square (num) :
    num = int (num)
    print("Square Number Is:",(num * num))
def is_prime (num):
    num =int(num)
    i = 2
    j = 0
    while (i <= (num/2)):
       if (num % i == 0):
          j = 1
          i = i + 1
    if (j == 1):  
       print("Not Prime Number:")
    else:
       print("Prime Number:") 

    #Task8: Create a Student Dictoniry and Print Information
    def task8 ():
         student = {
       "name": "Nazmunnaher",
        "age":    37,
        "grade":  "A"
    } 
         student["course"] = "CSE"
    print("keys in the dictionary:",student.keys())
    print("key_value paris:")
    for key , value in student.items():
       print(key, value)
       task8()
       
       



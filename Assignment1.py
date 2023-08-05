name = " Nazmun"
age =      37
print(name)
print(age)
print("My Name Is" + name + " and I am"  "  years old" ) 


# Task2: Data types and type conversation
num1 = 10
num2 = 10.5
num1_float = float(num1)
num2_int =int(num2)
print("num1:" + str(num1))
print("num1_float:" + str(num1_float))
print("num2:" +str(num2))
print("num2_int:" + str(num2_int))

#Task3: String Manipulation
sentence = "Python Programming Is Fun!\""
print("Length of" + sentence + "is:" + str(len (sentence)))
print("8th character of" + sentence + "is:" + str(sentence[8]))
substring = sentence[:7]
print("I enjoy it!" + substring)

# Task4: Lists and List Manipulation
fruits = ["apple","banana","chery","date"]
fruits.append("grape")
fruits.remove("banana")
print(len(fruits))
sliced_fruits=fruits[2:4]
print(sliced_fruits)
extra_fruits = ["kiwi", "lemon"]
combined_fruits = sliced_fruits + extra_fruits
print(combined_fruits)


#Task7
def calculate_square(num):
    return num*num
 
def is_prime(num):
    flag = True
    for n in range(2,num):
           if num % n == 0:
                flag = False
                break;
    return flag
print(calculate_square(7))
print(is_prime(29))
calculate_square()
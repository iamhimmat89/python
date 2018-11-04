print("Hello World..!!!")

# Variables
char_name = "John"
char_age = 35
is_male = True
phrase = "There was a man named " + char_name + ", He was " + str(char_age) + " years old."

# String
print("String:", phrase)
print("Length of String:", len(phrase))
print("String replace:", phrase.replace("man", "guy"))

# Arithmetic Operations
addition = 3 + 5.4
print("Addition:", addition)
print("Subtraction:", 10 - 4)
print("Modulus:", 10 % 3)
print("Division:", 10 / 3)
print("Integer Division:", 10 // 3)
print("Exponent:", 2 ** 3)

# List
list = [2, 5, 7, 8, 9, 6]
print(list)
print(list[0])
print(list[-1])
print(list[1:])
print(list[:4])
print(list.index(7))
list.append(3)
list.insert(1, 4)
print(list)
list.remove(4)
list.pop()
print(list)
list.sort()
print(list)

# Tuple
tuple_coordinate = (4, 5)
print(tuple_coordinate[0])

# Dictionary
month_dictionary = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}
print(month_dictionary["Feb"])
print(month_dictionary.get("Mar"))
print(month_dictionary.get("Apr", "Not a valid month"))

# if-elif-else Statements
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("You are male and not tall")
else:
    print("You are neither male nor tall")

# while loops
i = 0
while i <= 5:
    print(i)
    i += 1

# for loops
city = ["Mumbai", "Pune"]
for letter in city:
    print(letter)

# Exception Handling
try:
    ans = 10 / 0
    print(ans)
except ZeroDivisionError as err:
    print("Zero Division Error:", err)
except Exception as e:
    print("something went wrong", e)
finally:
    print("resource close")


# Functions
def first_fun(name):
    print("Function first_fun.. Param " + name)


first_fun("test")


def cube(num):
    return num * num * num


result = cube(5)
print(result)

# User input
number = int(input("Enter Number: "))
print(number)

# File Handling
file_read = open("README.md", 'r')
print(file_read.read())

file_write = open("testData", 'w')
file_write.write("This is test data file")
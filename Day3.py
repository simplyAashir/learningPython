"""
square = lambda x: x**2
print(square(5))

add = lambda a, b: a+b
print(add(3, 4))

students = [("Ali", 3.5), ("Sara", 3.8), ("John", 3.2)]
students.sort(key=lambda s: s[1])
print(students)

#--------------PRACTICE PROBLEMS--------------

def calculator():
    print("=====Simple Calculator=====")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    if op == "+":
        return a, op, b, a+b
    elif op == "-":
        return a, op, b, a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0:
            print( "Division by zero not allowed")
            return
        else:
            return a, op, b,a/b
    elif op == "%":
        return a, op, b, a%b
    else:
        print("Invalid operator")
        return
res = calculator()
if res:
    a, op, b, r = res
print(f"{a} {op} {b} = {r}")
"""
#===========Check prime number===========
"""
def is_prime(n):
    if n <= 1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n//2)+1, 2):
        if n % i == 0:
            return False
        
        return True
    

num = int(input("Enter a number: "))
if is_prime(num):
     print(f"{num} is a prime number.")
else:
     print(f"{num} is not a prime number.")


#==================FizzBuzz==============
for i in range(1, 101):
    if i % 3 == 0 and i %5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#==============IsPallindrome=================
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
str = input("Enter a string: ")
result = is_palindrome(str)
if result:
    print(f"{str} is a palindrome.")    
else:
    print(f"{str} is not a palindrome.")
#=================Count vowels===================
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count+=1
            return count
print(count_vowels("Hello World"))

#=================Reverse string====================
def reverse_string(s):
    return s[::-1]
str = input("Enter a string: ")
result = reverse_string(str)
print(f"Reversed string: {result}")
 """
#==================================================
#=====================LISTS========================
#==================================================
empty = []
print(empty)
marks = [85, 90, 78, 92]
print("MARKS: " + str(marks))
fruits = ["apple", "banana", "cherry"]
print("FRUITS: " + str(fruits))
mixed = [10, "abc", 4.35, True, None]
print("MIXED: " + str(mixed))
numbers = [1, 2, 2, 3, 3, 3, 4]
print("NUMBERS: " + str(numbers))
print("Length of marks list: " + str(len(marks)))
squares = list(range(1, 6))
print("SQUARES: " + str(squares))
chars = list("FAST")
print("CHARS: "+str(chars))
#------------List indexing -------------

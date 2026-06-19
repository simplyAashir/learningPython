import random
"""age = int(input("Enter ur age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
    #-----
    marks = int(input("Enter marks(0-100): "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif (marks >= 70):
        print("Grade: C")
    elif (marks >= 60):
        print("Grade: D")
    else:
        print("Grade: F")

#----Nested if
usrname = input("Enter username: ")
password = input("Enter password: ")
if usrname == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Incorrect pasword")
else:
    print("Unknown user")

#-------Logical operators
age = 21
has_degree = True
if age>= 21 and has_degree:
    print("Eligible for job")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

is_raining = False
if not is_raining:
    print("Go for a walk!")

score = 75
attendance = 80
if (score >= 50 and attendance >= 75):
    print("Passed the course")
elif (score >= 50 and attendance < 75):
    print("Failed due to low attendance")
else:
    print("Failed due to low score")

    #--------------Ternary
status = "adult" if age >= 18 else "Minor"
x = 10
print("x is even" if x %2 == 0 else "x is odd")

num = -15
absolute = num if num >= 0 else -num
print(absolute)
"""

#===========LOOPS==========
"""
for i in range(5):
    print(i)

diff = "-"*30
print(diff)
for i in range(1, 6):
    print(i)
print(diff)
for char in "FAST":
    print(char)
    print(diff)
total = 0
for i in range(1, 11):
    total += i
    print("Sum:", total)
print(diff)
num=int(input("Enter number for table:"))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print(diff)
for i in range(1, 6):
    print("*" * i)
    print(diff)
    print(diff)
#---------While Loop--------
count = 1
while count <= 5:
    print(count)
    count+=1
age = -1
while age < 0:
    age = int(input("Enter a +ve age:"))
    print("Your age is: ", age)

    """
#------------------
"""
secret = random.randint(1, 100)
attempts = 0
guess = None
while guess != secret and attempts < 5:
    guess = int(input("Guess the number: "))
    attempts+=1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You guessed the number in", attempts, "attempts.")
if guess != secret:
    print("Sorry, you've used all attempts. The secret number was", secret) 

    #---------Break, continue, pass--------
    for i in range(10):
        if i == 5:
            break
        print(i)
        for i in range(10):
            if i %2 == 0:
                continue
            print(i)

for i in range(5):
    if i == 3:
        pass
print(i)

#First prime no greater than 50
for num in range(51, 200):
    is_prime = True
for divisor in range(2, num):
    if num % divisor == 0:
        is_prime = False
        break
    if is_prime:
        print("First prime > 50:", num)
        break
     """   
"""

#---------PRACTICE PROBLEMS--------
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
if marks >= 85 and attendance >= 80: print("Scholarship awarded")
else:
    print("Not eligible")

secret = "fast123"
i = 0
while i < 3:
    secInp = input("Enter the password: ")
    if secInp == secret:
        print("Access Granted")
        break
    else:
        print("Wrong password")
i+=1
if i == 3:
    print("Access denied")
    
evenC = oddC = 0
for i in range(1, 11):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        evenC += 1
    else:
            oddC += 1
print("Number of even numbers:", evenC)
print("Number of odd numbers:", oddC)

#----------------------
n = int(input("Enter a number: "))
for i in range(1, n):
     print("*" * i)
     """
#================================
def greet():
    print("Hello, Welcome to python!")

greet()
greet()

def greetPerson(name):
    print(f"Hello, {name}")

greetPerson("Ali")

def add(a, b):
    return a+b

result = add(5,3)


def circle_area(rad):
    pi = 3.14159
    area = pi*rad**2
    return area

a = circle_area(5)
print(f"Area: {a:.2f}")


print("-"*40)
def Power(base, exp=2):
    return base**exp
print(Power(4))
print(Power(4, 3))

def studentInfo(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

studentInfo("Ali", 20, "B")

def min_max(numbers):
    return min(numbers), max(numbers)
low, high = min_max([3, 1, 7, 2, 9, 4])
print(f"Min: {low}, Max: {high}")

x = 100
def show():
    y = 50
    print(x)
    print(y)

show()
print(x)

<<<<<<< HEAD
# comments in python
"""
------------
--------------
"""

"""
print("Comments have no affect")
name = "Aashir"
age = 20
gpa = 3.5
is_Student = True
print(name)
print(age)
print(gpa)
print(is_Student)
# Printing with a label
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is Student:", is_Student)

x = y = z = 0
print(x, y, z)
#swapping two variables
a = 10
b = 20
a, b= b, a #explain this swapping technique
print("a =", a)
print("b =", b)
#-----------------
print(name, age, gpa, is_Student)
#-------------------------------Week 2-------------------
"""
x = 100
y = -50
print(type(x))
print(type(y))
pi = 3.14159
temp = -2.5
print(type(pi))
print(type(temp))
name = "Python"
university = 'FAST'
print(type(name))
print(type(university))
passed = True
failed = False
print(type(passed))
print(type(failed))
result = None
print(type(result))
"""
#-----------------------Type casting--------
str = "21" #string to int
num = int(str)
print(num)

x = int(3.5)  #float to int
print(x)

num2 = 42
str2 = str(num2) #int to string
print("Number is:" + str2)

price = float("185.4") #string to float
print(price)

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool([])) 
print(bool(None))


#---------------Arithmetic operators----------------
a = 13
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor division
print(a%b)

#-----------INPUT/OUTPUT----------------
name = input("Enter ur name: ")
print("Hello, "+name)
age = int(input("Enter ur age:"))
print("Next year, you will be", age+1, "years old.")
gpa = float(input("Enter ur gpa: "))
print("your gpa is:", gpa)
#----
name = "Ali"
age = 25
gpa = 3.75
print(f"Name: {name}, Age: {age}, GPA: {gpa}")
print(f"In 5 years, u will be {age+5}")

print("Name: {}, Age: {}, GPA: {}".format(name, age, gpa))
print("In 5 years, u will be {}".format(age+5))

pi = 3.14159
print(f"Pi = {pi:.2f}")
print(f"Pi = {pi:.4f}")

name = input("Enter your name:")
age = int(input("enter ur age: "))
gpa = float(input("Enter your gpa: "))
print(f"Student Name: {name}, "f"Current Age: {age}, Age after 5 years: {age+5}, GPA: {gpa:.2f}")



pName = input("Product: ")
quantity = int(input("Quantity: "))
ppi = float(input("Price per item: "))
print(f"Product: {pName}, Quantity:{quantity}, Price per item: {ppi}, Total Bill: {quantity*ppi}")
"""

#---------------String manipulation--------------
name = "Python"
print(name[0])
print(name[1])
print(name[-1])
print(name[-2]) #o is second last character
print(len(name))  #length = 6

#name[0] = "j" #error because strings are immutable
first = "FAST"
last = "NUCES"
full = first+" "+last #string concatenation
print(full) 

line = "-" * 30
print(line) #line repetition 

#---------String Slicing------------
text = "Hello, World"
print(text[0:5])
print(text[7:])
print(text[:5])
print(text[-6:-1])
print(text[::2])
print(text[::-1])

email = "ali@nu.edu.pk"
at_index = email.index("@")
domain = email[at_index+1:]
print(domain)

text = "Hello, python world"
print(text.upper())
print(text.lower())
print("hello".capitalize())
print("hello world".title())
print(text.strip())
print(text.lstrip())
print(text.rstrip())

s = "I love Java. Java is great."
print(s.find("Java"))
print(s.rfind("Java"))
print(s.count("Java"))
print(s.replace("Java", "Python"))

sentence = "FAST Uni Islamabad"
words = sentence.split(" ")
print(words)
joined = "-".join(words)
print(joined)
#check methods
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("  ".isspace())
print("hello".startswith("h"))
print("hello".endswith("lo"))

print("Python" in "I love Python")
print("Java" not in "I love Python")


=======
# comments in python
"""
------------
--------------
"""

"""
print("Comments have no affect")
name = "Aashir"
age = 20
gpa = 3.5
is_Student = True
print(name)
print(age)
print(gpa)
print(is_Student)
# Printing with a label
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is Student:", is_Student)

x = y = z = 0
print(x, y, z)
#swapping two variables
a = 10
b = 20
a, b= b, a #explain this swapping technique
print("a =", a)
print("b =", b)
#-----------------
print(name, age, gpa, is_Student)
#-------------------------------Week 2-------------------
"""
x = 100
y = -50
print(type(x))
print(type(y))
pi = 3.14159
temp = -2.5
print(type(pi))
print(type(temp))
name = "Python"
university = 'FAST'
print(type(name))
print(type(university))
passed = True
failed = False
print(type(passed))
print(type(failed))
result = None
print(type(result))
"""
#-----------------------Type casting--------
str = "21" #string to int
num = int(str)
print(num)

x = int(3.5)  #float to int
print(x)

num2 = 42
str2 = str(num2) #int to string
print("Number is:" + str2)

price = float("185.4") #string to float
print(price)

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
print(bool([])) 
print(bool(None))


#---------------Arithmetic operators----------------
a = 13
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor division
print(a%b)

#-----------INPUT/OUTPUT----------------
name = input("Enter ur name: ")
print("Hello, "+name)
age = int(input("Enter ur age:"))
print("Next year, you will be", age+1, "years old.")
gpa = float(input("Enter ur gpa: "))
print("your gpa is:", gpa)
#----
name = "Ali"
age = 25
gpa = 3.75
print(f"Name: {name}, Age: {age}, GPA: {gpa}")
print(f"In 5 years, u will be {age+5}")

print("Name: {}, Age: {}, GPA: {}".format(name, age, gpa))
print("In 5 years, u will be {}".format(age+5))

pi = 3.14159
print(f"Pi = {pi:.2f}")
print(f"Pi = {pi:.4f}")

name = input("Enter your name:")
age = int(input("enter ur age: "))
gpa = float(input("Enter your gpa: "))
print(f"Student Name: {name}, "f"Current Age: {age}, Age after 5 years: {age+5}, GPA: {gpa:.2f}")



pName = input("Product: ")
quantity = int(input("Quantity: "))
ppi = float(input("Price per item: "))
print(f"Product: {pName}, Quantity:{quantity}, Price per item: {ppi}, Total Bill: {quantity*ppi}")
"""

#---------------String manipulation--------------
name = "Python"
print(name[0])
print(name[1])
print(name[-1])
print(name[-2]) #o is second last character
print(len(name))  #length = 6

#name[0] = "j" #error because strings are immutable
first = "FAST"
last = "NUCES"
full = first+" "+last #string concatenation
print(full) 

line = "-" * 30
print(line) #line repetition 

#---------String Slicing------------
text = "Hello, World"
print(text[0:5])
print(text[7:])
print(text[:5])
print(text[-6:-1])
print(text[::2])
print(text[::-1])

email = "ali@nu.edu.pk"
at_index = email.index("@")
domain = email[at_index+1:]
print(domain)

text = "Hello, python world"
print(text.upper())
print(text.lower())
print("hello".capitalize())
print("hello world".title())
print(text.strip())
print(text.lstrip())
print(text.rstrip())

s = "I love Java. Java is great."
print(s.find("Java"))
print(s.rfind("Java"))
print(s.count("Java"))
print(s.replace("Java", "Python"))

sentence = "FAST Uni Islamabad"
words = sentence.split(" ")
print(words)
joined = "-".join(words)
print(joined)
#check methods
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("  ".isspace())
print("hello".startswith("h"))
print("hello".endswith("lo"))

print("Python" in "I love Python")
print("Java" not in "I love Python")


>>>>>>> 6a741136450745395363a46bb1e88bc2b0f49b9d

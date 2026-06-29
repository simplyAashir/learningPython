#------Iterating through a list-------
#---1: Direct
alp = ['a','b','c']
for i in alp:
    print(i)
#---2: index-based
for i in range(len(alp)):
    print(alp[i])
#---3: to get index and value
for index, value in enumerate(alp):
    print(f"{index}: {value}")
#---4: To start index from particular number, use start parameter
for index, fruit in enumerate(alp, start=1):
    print(f"{index}: {fruit}")

names = ["Ali", "Sara", "Ahmed"]
scores = [95, 85, 76]
# Iterates two lists in parallel using zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")

#---- Combines in form of list of tuples
combined = list(zip(names, scores))
print(combined)
    
#========List Comprehensions========
# it creates a new list in a single line of code
#--Normal way--
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

#--List Comprehension way--
squares = [i**2 for i in range(1, 11)]
print(squares)

even_squares = [i**2 for i in range(1, 11) if i%2 == 0]
print(even_squares)

fruits = ["apple", "banana", "mango"]
upper_fruits = [f.upper() for f in fruits]
print(upper_fruits)

marks = [95, 32, 76]
passe = [mark for mark in marks if mark >= 60]
print(passe)

res = ["Pass" if mark >= 60 else "Fail" for mark in marks]
print(res)

#------Flatten a 2d list into 1d-------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12]]
flat = [num for r in matrix for num in r]
print(flat)


#---------Mathematical operations on list---------
nums = [1,2,3, 4, 5]
print(sum(nums))
print(max(nums))
print(min(nums))
print(len(nums))
avg = sum(nums)/len(nums)
print(avg)

nums = [1, 2, 3, 4, 5]
doubled = [num*2 for num in nums]
print(doubled)

#concatenation and repetitions
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#--------List as stack and Queue--------
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) # [1, 2, 3]
stack.pop()
print(stack) # [1, 2]
stack.pop()
print(stack) # [1]

#--Queue--
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue) # deque([2, 3])
queue.popleft()
print(queue) # deque([3])

#============TUPLES===========
empty = ()
single = (43, )
wrong = (43) #Not a tuple, just an integer
print(type(empty)) # <class 'tuple'>
print(type(single)) # <class 'tuple'>
print(type(wrong)) # <class 'int'>

coordinates = (10.4, 44.2)
rgb = (255, 128, 0) 
student = ("Ali", 20, "CS")
print(coordinates[0])
print(student[0])
print(student[-1])
print(rgb[1:])
print(len(student))
#Tuples are immutable, but u can change whole tuple by reassigning
coordinates = (20.5, 30.6)
print(coordinates)
#----Tuple methods-----
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))
print(t.index(3)) #index of first occurrence

#---------Tuple packing and unpacking---------
person = "ali", 20, "CS" 
print(person) # ('ali', 20, 'CS')
print(type(person)) # <class 'tuple'>
#--unpacking
name, age, major = person
print(name)
print(age)
print(major)

def get_min_max(num):
    return min(num), max(num)

first, *rest = (1, 2, 3, 4, 5)
print(first) # 1
print(rest) # [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
print(first) # 1
print(middle)   # [2, 3, 4]
print(last)    # 5


a, b = 10, 15
a, b = b, a
print(a, b) # 15, 10    

#=========Dictionaries========
student = {
    "name": "Ali",
    "age": 20,
    "gpa": 3.85,
    "uni": "FAST",
    "passed": True
}
print(student)
print(student['name'])
print(student['gpa'])
print(student.get('age'))
print()

print(student.get("age")) # 20
print(student.get("phone")) #it will print NONE (no error)
print(student.get("phone", "Not Available")) # it will print "Not Available"

#---Modifying values---
student['gpa'] = 3.58
print(student["gpa"]) # 3.58
student['semester'] = 5
print(student["semester"]) 

del student['passed']
print
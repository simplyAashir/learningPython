#-----------List Indexing--------------
marks = [95, 85, 76, 88, 92]
print(marks[0])
print(marks[1]) 
print(marks[4]) #92
print(marks[-1]) #92
print(marks[-2]) #88
print(marks[-5]) #95
marks[2] = 55
print(marks)
name = "Ali"
#name[0] = "M" #error, as strings are immutable
students = ["Ali", "Sara", "Ahmed"]
students[1] = "Babar"
print(students) #['Ali', 'Babar', 'Ahmed']
#------------List Slicing---------------
marks = [5, 6, 3, 9, 2, 8]
print(marks[0:3]) # [5, 6, 3]
print(marks[2:5]) # [3, 9, 2]
print(marks[:3]) # [5, 6, 3]
print(marks[4:]) # [2, 8]
print(marks[:]) # entire list
#with step
print(marks[::2]) #every 2nd entry
print(marks[1::2]) #every 2nd entry starting from index 1
print(marks[::-1]) #reverse the list
sorted_marks = sorted(marks, reverse=True)
print(sorted_marks[0:3])
#This will gives us top 3 marks 

#----------------List Methods---------------
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)
fruits.extend(["grape", "kiwi"])
print(fruits)
fruits.insert(1, "pear")
print(fruits)
fruits.remove("banana")
print(fruits) 
fruits.pop() 
print(fruits)
fruits.pop(2) #removes the element at index 2
print(fruits)
fruits.clear()
print(fruits) # []

# ===searching in list===
num = [10, 20, 30, 40, 20]
print(num.index(20)) # returns the index of the first occurrence of 20
print(num.count(20)) # returns the count of 20 in the list
print(20 in num) # checks if 20 is in the list, returns True

#===Sorting a list===
nums = [5, 2, 9, 1, 5, 6]
nums.sort()
print(nums) # [1, 2, 5, 5, 6, 9]
nums.sort(reverse=True)
print(nums) # [9, 6, 5, 5, 2, 1]
nums.reverse() #reverses current order
print(nums) # [1, 2, 5, 5, 6, 9]
original = [5,2, 6, 1]
new_sorted = sorted(original) #returns a new sorted list
print(original)
print(new_sorted)

#-------Copying---------
a = [1, 2, 3]
b = a # b is a reference to a, not a copy
b.append(4)
print(a) # [1, 2, 3, 4]
#To make a copy, use the copy() method or list slicing
c = a.copy() #independent copy
c.append(5)
print(a) # [1, 2, 3, 4]
print(c) # [1, 2, 3, 4, 5]
#another way to copy a list is using slicing
d = a[:] #independent copy
d.append(6)
print(a) # [1, 2, 3, 4]
print(d) # [1, 2, 3, 4, 6]

#=======Iterating through a list========
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("-"*20)
for i in range(len(fruits)):
    #print(fruits[i])
    print(f"{i}: {fruits[i]}")
print("-"*20)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for index, fruit in enumerate(fruits):
    print(f"{index}")

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

names = ["Ali", "Sara", "Ahmed"]
scores = [95, 85, 76]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

combined = list(zip(names, scores))
print(combined)

#--------List Comprehensions--------
squares = [i**2 for i in range(1, 11)]
print(squares)

ev_squares = [i**2 for i in range(1, 11) if i%2 == 0]
print(ev_squares)

fruits = ["apple", "banana", "mango"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

marks = [45, 68, 90, 55, 72]
passing = [m for m in marks if m >=60]
print(passing)


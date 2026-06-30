student = {
    "name": "ali",
    "age": 20,
    "gpa": 4,
    "uni": "FAST",
    "passed": True
}
print(student)
print(student['name'])
print(student['gpa'])
print(student.get('age'))
print(student.get('phone'))
print(student.get('phone', 'not available'))
student['gpa'] = 3.8
print(student['gpa'])
del student['passed'] 
print(student)
#------Remove and return a value
age = student.pop('age')
print(age) # 20
print(student) # {'name': 'ali', 'gpa': 3.8,
#check if key exists
print('name' in student)

#---------Dictionary methods-----------
stu = {
    "name": "Ali",
    "age": 20,
    "gpa": 3.85,
    "city": "Lahore"
}
print(stu.keys())
print(stu.values())
print(stu.items())
#iterating through a dictionary
for key in stu:
    print(key)
for key in stu.keys():
    print(key, ":", stu[key])
for value in stu.values():
    print(value)
for key, value in stu.items():
    print(f"{key} : {value}")
extra = {
    "semester": 5,
    "gpa": 2.3
}
stu.update(extra)
print(stu)
print(stu.get("gpa")) 
print(stu.get("semester"))
#-------copying a dictionary
orig = {"x": 1, "y": 2}
copy = orig.copy()
copy["z"] = 3
copy["x"] = 10
print(copy) # {'x': 10, 'y': 2, 'z': 3}
print(orig) # {'x': 1, 'y': 2}

d = {"a": 1}
d.setdefault("b", 2) # if key "b" does not exist, it will be added with value 2
d.setdefault("a", 10) # if key "a" exists, it will not change its value
print(d) # {'a': 1, 'b': 2}
d.clear() # removes all items from the dictionary
print(d) # {}
#============Dictionary comprehension==========
squares = {n: n**2 for n in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped) # {1: 'a', 2: 'b', 3: 'c'}

students={"Ali": 3.4, "Ahmed": 3.8, "Sara": 3.9}
top_students = {name: gpa for name, gpa in students.items() if gpa >= 3.5}
print(top_students) # {'Ahmed': 3.8, 'Sara': 3.9}
#---Word frequency counter
text = "the cat sat on the mat the cat"
words = text.split()
freq = {word: words.count(word) for word in set(words)}
print(freq) # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

#================SETS==========
print("================SETS================")
num = {1,2,3,4,5}
print(num)
with_dups = {1,2,3,4,5,1,2,3}
print(with_dups) #Duplicates are automatically removed

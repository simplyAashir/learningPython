#================SETS===============
"""
nums = {1, 2, 3, 4, 5}
print(nums)
#duplicates are automatically removed
dup_nums = {1, 2, 3, 4, 5, 1, 2, 3}
print(dup_nums) # {1, 2, 3, 4, 5}

empty_set = set() # {} creates an empty dictionary, not a set
empty_dict = {}
print(type(empty_set)) # <class 'set'>
print(type(empty_dict)) # <class 'dict'>

#create a set from a list
list_nums = [1, 2, 3, 4, 5, 1, 2, 3]
set_from_list = set(list_nums)
print(set_from_list) # {1, 2, 3, 4, 5}

#sets have no indexing or slicing, but you can iterate through them
for num in nums:
    print(num)
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits) # True
print("orange" in fruits) # False

s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}

s.add(2)
print(s) # {1, 2, 3, 4} - adding an existing element does nothing

s.discard(3)  #no error, if not found
print(s) # {1, 2, 4}

s.remove(2)   #error,if found
print(s) # {1, 4}

popped = s.pop() #removes and returns RANDOM element
print(popped)

#---------Set operations---------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A|B) # union {1, 2, 3, 4, 5, 6}
print(A.union(B)) # union {1, 2, 3, 4, 5, 6}
print(A&B) # intersection {3, 4}
print(A.intersection(B)) # intersection {3, 4}
print(A-B) # difference {1, 2}
print(A.difference(B)) # difference {1, 2}
#symmetric difference: elements in either A or B but not both
print(A^B) # symmetric difference {1, 2, 5, 6}
print(A.symmetric_difference(B)) # symmetric difference {1, 2, 5, 6}
c = {3, 4}
print(c.issubset(A)) # True
print(A.issuperset(c)) #True
print(A.isdisjoint({8, 9})) #True
print(A.isdisjoint({3, 4})) #False

#-------Remove duplicates while keeping order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
            return result
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(remove_duplicates(data)) # [3, 1, 4, 5, 9, 2, 6]
classA = {"Ali", "Ahmed", "Ayesha"}
classB = {"Sara", "Ali", "Ahmed"}
common = classA & classB
common = classA.intersection(classB)
print("in both classes:", common) # {'Ali', 'Ahmed'}
onlyA = classA - classB
onlyA = classA.difference(classB)
print("only in class A:", onlyA) # {'Ayesha'}

#==================NESTED DATA STRUCTURES================
#========================================================

#------Nested lists (2D matrix)--------
matrix = [
    [1, 2, 3], 
    [4, 5, 6], [7, 8, 9]]
print(matrix[0][1]) #2
print(matrix[2][0]) #7
#modifying a nested list
matrix[0][0] = 99
print(matrix) # [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

zeros = [[0 for j in range(3)]
         for i in range(3)]
print(zeros)

#Transpose of a matrix
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[original[j][i] for j in range(len(original))] for i in range(len(original[0]))] 
print(transpose) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#========List of dictionaries=========
students = [
    {"name": "Ali", "age": 20, "gpa": 3.8},
    {"name": "Ahmed", "age": 22, "gpa": 3.5},
    {"name": "Sara", "age": 21, "gpa": 3.9}
]
print(students[0]["name"])
print(students[2]["gpa"])
#----iterate and print all students----
for s in students:
    print(f"{s['age']} | {s['name']} | {s['gpa']}")

#Filter: students with gpa >= 3.5
top = [s for s in students if s["gpa"] > 3.5]
for s in top:
    print(f"{s['name']} | {s['gpa']}")

#sort by highest gpa
ranked = sorted(students, key = lambda s:s["gpa"], reverse = True)
for s in ranked:
    print(f"{s['name']}", s['gpa'])

#add a new student
students.append({"name": "Ayesha", "age": 23, "gpa": 3.6})
for s in students:
    if s["name"] == "Ayesha":
        s["gpa"] = 3.7
        break

avgGpa = sum(s["gpa"] for s in students) / len(students)
print(f"Avg GPA: {avgGpa:.2f}")

#----------Dicionary of lists----------
marks = {
    "Ali": [85, 90, 78],
    "Ahmed": [88, 92, 80],
    "Sara": [90, 85, 95]
}
print(marks["Ali"]) # [85, 90, 78]
print(marks["Ali"][1]) # 90
for name in marks:
    marks[name].append(90) # add a new mark for each student
    print(f"{name}: {marks[name]}")
#each student's average mark
for name, scores in marks.items():
    avg = sum(scores)/len(scores)
    print(f"{name}: {avg:.2f}")

#add a new student
marks["Hina"] = [88, 92, 85]
print(marks["Hina"]) # [88, 92, 85]

#=======================Practice Problems=========================
def find_duplicates(lst):
    seen = set()
    dupes = set()
    for num in lst:
        if num in seen:
            dupes.add(num)
        else:
                seen.add(num)
    return list(dupes)
numbers = [1, 2, 3,2, 4, 3, 5, 1]
print(find_duplicates(numbers)) # [1,2,3]
print(find_duplicates([1, 2, 4])) # []
print(find_duplicates([1, 1, 1, 1])) # [1]

def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    sorted_freq = sorted(freq.items(),
                         key=lambda x: x[1],
                         reverse=True)
    return sorted_freq

sentence = "the cat sat on the mat the cat"
print(word_frequency(sentence)) # [('the', 3), ('cat', 2), ('sat', 1), ('on', 1), ('mat', 1)]



"""
def are_anagrams(str1, str2):
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for char in s1:
        freq1[char] = freq1.get(char, 0)+1
    for char in s2:
        freq2[char] = freq2.get(char, 0)+1
    return freq1 == freq2
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
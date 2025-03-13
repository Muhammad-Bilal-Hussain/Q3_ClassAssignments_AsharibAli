# 1st Example (List (Mutable, Ordered))
fruits = ["apple", "banana", "mango"]

# List elements access
print(fruits[0])  # apple

# List add
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

# List update
fruits[1] = "grapes"
print(fruits)  # ['apple', 'grapes', 'mango', 'orange']

# 2nd Example (Loop Through List)
colors = ["red", "blue", "green"]

for color in colors:
    print(color)

# 3rd Example (Tuple (Immutable, Ordered))
coordinates = (10, 20, 30)

# Tuple ke elements access karna
print(coordinates[1])  # 20

# Tuple ko loop se print karna
for point in coordinates:
    print(point)

# 4th ezample (Tuple Unpacking)
person = ("Ali", 25, "Karachi")

name, age, city = person

print(name)   
print(age)   
print(city) 

# 5th Example (Dictionary (Key-Value Pairs, Mutable))
student = {
    "name": "Sara",
    "age": 22,
    "city": "Lahore"
}

# Dictionary ke element access kara
print(student["name"]) 

# Dictionary me value update
student["age"] = 23

# Naya key-value pair add
student["degree"] = "CS"

print(student)

# 6th Example (Loop Through Dictionary)
person = {
    "name": "Ahmed",
    "job": "Designer"
}

for key, value in person.items():
    print(f"{key}: {value}")

# 7th Example (Nested List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2nd row ke elements ko access kara
print(matrix[1])     
print(matrix[0][2])

# 8th Example (Dictionary Inside List (Real Example))
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 90},
    {"name": "Ahmed", "marks": 78}
]

# Har student ka name aur marks print karna
for student in students:
    print(f"{student['name']} scored {student['marks']} marks")
# This prints the name and marks of each student in the list students.



# 1st example (if Statement)
x = 10

if x > 5:
    print("x is greater than 5")
# This checks if x is greater than 5. If true, it prints the message. If false, nothing happens.

# 2nd example (if-else Statement)
age = 10

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# This checks if age is greater than or equal to 18. If true, it prints the first message. If false, it prints the second message.

# 3rd example (if-elif-else Statement)
marks = (int(input("Enter your marks: ")))

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")
# This checks if marks is greater than or equal to 90. If true, it prints the first message. If false, it checks if marks is greater than or equal to 70. If true, it prints the second message. If false, it prints the third message.

# 4th example (Nested if Statement)
num = int(input("Enter a number for check EVEN & ODD: "))

if num > 2:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# This checks if num is even. If true, it checks if num is divisible by 2. If true, it prints the first message. If false, it prints the second message. If false, nothing happens.

# 5th example (while Loop)
count = 1

while count <= 5:
    print("Count:", count)
    count += 1
# This checks if count is less than or equal to 5. If true, it prints the message. If false, nothing happens.
# count += 1 is used to increment the value of count by 1.

# 6th example (for Loop (with range))
for i in range(1, 6):
    print(i)
# This prints the numbers from 1 to 5.

# 7th example (for Loop (with list))
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# This prints the elements of the list fruits.

# 8th example (break Statement)
for i in range(1, 10):
    if i == 8:
        break
    print(i)
# This prints the numbers from 1 to 4. When i becomes 5, the loop is terminated using the break statement.

# 9th example (continue Statement)
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# This prints the numbers from 1 to 5 except 3. When i becomes 3, the loop skips the iteration using the continue statement.

# 10th example (pass Statement)
x = 5

if x > 0:
    pass
else:
    print("x is negative")
# This checks if x is greater than 0. If true, nothing happens. If false, it prints the message.
# The pass statement is used to do nothing when the condition is true. It is used as a placeholder for future code.
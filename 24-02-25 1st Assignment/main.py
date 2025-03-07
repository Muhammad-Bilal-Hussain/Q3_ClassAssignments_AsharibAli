#1 =======> int(integer) function is used to only numbers.
# 1 example is given below.
# number = 40
# print(type(number))

# 2 example is given below.
# number = int(input("Enter the number: "))
# print(number)

#2 =======> float function is used to only decimal numbers.
# 1 example is given below.
# number = 40.5
# print(type(number))

# 2 example is given below.
# number = float(input("Enter the number: "))
# print(number)

#3 =======> str(string) function is used to for text data in " " double coats.
# 1 example is given below.
# name = "Muhammad Ali"
# print(type(name))

# 2 example is given below.
# name = str(input("Enter the name: "))
# print(name)


#4 =======> bool(boolean) function is used to for True or False.
# 1 example is given below.
# status = True
# print(type(status))

# 2 example is given below.
# status_input = input("Enter the Boolean status (True/False): ")

# # Check if input is exactly 'True' or 'False'
# if status_input == "True":
#     status = True
# elif status_input == "False":
#     status = False
# else:
#     raise ValueError("Invalid input! Please enter only 'True' or 'False'.")

# print(f"Boolean status: {status}")
# print(type(status))



#5 =======> (list) function is used to for multiple values in [] square coats.
# 1 example is given below.
# names = ["Ali", "Ahmed", "Asad"]
# print(type(names))

# # 2 example is given below.
# names = []
# name1 = input("Enter the 1st name: ")
# name2 = input("Enter the 2nd name: ")
# name3 = input("Enter the 3rd name: ")

# names.append(name1)
# names.append(name2)
# names.append(name3)
# print(names)


#6 =======> (tuple) function is used to for multiple values in () round braket.
# 1 example is given below.
# names = ("Ali", "Ahmed", "Asad")
# print(type(names))

# # 2 example is given below.
# colorName = input("Enter the 1st color name seprated by comma: ")
# sepComma = tuple(colorName.split(", "))

# print("Tuple: ", sepComma)
# print("color Names Type", type(sepComma))

#7 =======> (set) function is used to for multiple values in {} curly braket and it will not allow to duplicate values. it is unoder and set is mutable this is element is immutale.

# 1 example is given below.
# names = {"Ali", "Ahmed", "Asad", 1, 3, 2,4,4}
# print(names)
# print(type(names))

# 2 example is given below.
# marks = set()

# marks.add(input("Enter the 1st number: "))
# marks.add(input("Enter the 2nd number: "))
# marks.add(input("Enter the 3rd number: "))

# print(marks)
# print(type(marks))

# 3 example is given below.
# my_frozenset = frozenset([1, 2, 3, 4])

# Yeh line error dega kyunki frozenset immutable hai
# my_frozenset.add(5)  <-- Error
# print(my_frozenset)
# print(type(my_frozenset))


#8 =======> (dict) function is used to for multiple values in {} curly braket and  Key-value pairs (e.g., {'name': 'Ali', 'age': 20}). it is mutable.
#1 example is given below.
# person = {
#     "name": "Ali",
#     "age": 20,
#     "qualification": "Matric"
# }
# print(person)
# print(type(person))

# # 2 example is given below.
# StdDict = {}

# x = int(input("Std Phyc marks: "))
# StdDict.update({"std Phyc: ": x})

# x = int(input("Std Computer marks: "))
# StdDict.update({"std Computer: ": x})

# x = int(input("Std Math marks: "))
# StdDict.update({"std Math: ": x})

# print(StdDict)


# 9 ======> (Range) function is used to for range of numbers.
# 1 example is given below.
# for i in range(10):
#     print(i)

# 2 example is given below. start , stop, step
# for i in range(0, 10, 2):
#     print(i)

# 10 ======> (None) function is used to for no value.
# 1 example is given below.
# x = None
# print(x)

#11 ======> (bytes) function is used to for bytes data.Byte literals likhne ke liye b'' use hota hai. Har element 0 se 255 ke beech me hota hai (1 byte = 8 bits).
# 1 example is given below.
# my_bytes = b'hello'
# print(my_bytes)
# print(type(my_bytes))


# 2 example is given below.
# data = [62, 64, 66, 68]
# byte_data = bytes(data)
# print(byte_data)


# 12 ======> (Bytearray) Mutable hoti hai (aap elements ko change kar sakte ho). bytearray() function ke through banate hain.
# 1 example is given below.
# arr = bytearray([65, 66, 67])
# arr[1] = 68
# print(arr)
# print(type(arr))

# 2 example is given below.
# arr = bytearray(b'abc')
# arr.append(100)     # ASCII value of 'd'
# arr.extend([101])   # ASCII value of 'e'
# print(arr)
# print(type(arr))


# 13 ======> (memoryview) function is used to for memoryview object that can be used to view the memory of an object.
# 1 example is given below.
# data = bytearray(b'hello')
# view = memoryview(data)
# print(view[0])   # ASCII of 'h'
# print(type(view))

# 2 example is given below.
# data = bytearray(b'world')
# view = memoryview(data)
# view[1] = 111    # Change 'o' to 'o' (ASCII 111)
# print(data)


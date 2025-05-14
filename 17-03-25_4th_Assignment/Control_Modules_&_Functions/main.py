import math #this is python's built-in math module
import time #this is python's built-in time module

print(math.sqrt(25))

def add(x, y):
    return x + y

def name():
    return "John Doe"


print("Start")
time.sleep(2)  # waits for 2 seconds
print("End")

# type alias (type alias rename karn ke liye use hota hai # type alias ka use karne se code ko samajhna asan hota hai)
import math as mt

print(mt.sqrt(25))  # using the alias 'mt' instead of 'math'




# Import Specific Functions or Variables (from ... import ...)

from math import sqrt, pi
print(sqrt(25))  # using the imported function directly
print(pi)  # using the imported variable directly





# ==============================Famous Third-Party Libraries Examples:=============================

# Library Name	Use:
# requests	= API call karne ke liye
# numpy	= Scientific calculations
# pandas	= Data analysis
# matplotlib =	Graphs/plots banane ke liye
# flask = 	Web applications ke liye
# Django =	Full web framework


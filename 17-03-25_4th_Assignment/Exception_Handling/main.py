# Exception Handling with try, except, else, and finally"
# Python me "Exception Handling" ka matlab hota hai error ko handle karna — taake program crash na ho aur user ko proper message mile.

# ✅ Exception handling kyu zaroori hai?
# 1. Program ko Crash hone se bachata hai
# Agar koi galti ho jaye (jaise zero se divide ya file na mile), to program turant band na ho, balkay error handle ho jaye smoothly.

# 2. Graceful Recovery
# User ko samajhne wala message milta hai, na ke koi scary error.

# Example:
# Instead of showing:
# ZeroDivisionError: division by zero
# You show:
# "Bhai 0 se divide nahi hota!"

# 3. Code Clean aur Samajhne Layak Banta Hai
# Error handling logic alag hoti hai aur main kaam alag, is se code clean aur maintainable hota hai.

# 4. Resources ka Proper Use aur Close Karna
# Agar file kholi ho ya internet connection use ho raha ho, aur beech me error aa jaye — to finally block se tum ensure kar sakte ho ke file ya connection properly close ho jaye.

# 🧠 try, except, else, finally kya hai?
# 🔹 try:
# Yahan wo code likhtay hain jahan error aane ka chance hota hai.

# 🔹 except:
# Agar try block me error aata hai, to ye chalega. Yahan error handle karte hain.

# 🔹 else:
# Agar try block successfully chal jaye (koi error na aaye), to else block chalega.

# 🔹 finally:
# Ye hamesha chalta hai — chahe error aaye ya na aaye. Mostly cleanup ke liye use hota hai (file close waghera).

# 1. Basic Example (Try-Except: Division Error python Copy Edit)
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Zero se divide nahi ho sakta")

# 2. Try-Except: Invalid Input (ValueError)
try:
    age = int(input("Apni age likho: "))
    print("Tumhari age:", age)
except ValueError:
    print("Error: Sirf number likho, text nahi")

# 3. Try-Except-Finally: File Handling 
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File nahi mili")
finally:
    print("Yeh block hamesha chalega")

# 4. Try-Except with Multiple Exceptions

try:
    a = int(input("Number: "))
    b = int(input("Divide by: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Zero se divide nahi ho sakta")
except ValueError:
    print("Error: Sirf number likho")

# 5. Custom Exception Raise Karna
def check_age(age):
    if age < 18:
        raise Exception("Underage ho bhai, allowed nahi")
    else:
        print("Welcome!")

try:
    check_age(15)
except Exception as e:
    print("Error:", e)


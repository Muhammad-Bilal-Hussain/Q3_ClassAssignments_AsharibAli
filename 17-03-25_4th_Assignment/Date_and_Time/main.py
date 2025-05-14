# Example 1: Math Functions (sqrt, pow)
import math

print(math.sqrt(16))     # 4.0
print(math.pow(2, 3))    # 8.0

#  Example 2: Math Constants (pi, e)
import math

print(math.pi)    # 3.14159...
print(math.e)     # 2.71828...

# Example 3: Date aur Time lena (current date & time)
import datetime

now = datetime.datetime.now()
print("Date and Time:", now)

# Example 4: Sirf Date ya Time lena

import datetime

today = datetime.date.today()
print("Only Date:", today)

current_time = datetime.datetime.now().time()
print("Only Time:", current_time)

# Example 5: Calendar Print Karna
import calendar

print(calendar.month(2025, 5))  # May 2025 ka calendar

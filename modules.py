# #import standard math module
# import math
# print(math.sqrt(16))

# from math import pi
# print(pi)

# from math import sqrt
# print(sqrt(49))

# #renaming modules for convenience
# import math as m
# print(m.pi)

# #random module - helps us generate random numbers
# import random
# print(random.randint(1,6))

# import datetime
# today = datetime.datetime.now()
# print(today)

# today = datetime.date.today()
# print(today)

# import calendar
# print(calendar.month(2024,2))
# print(calendar.isleap(2024))

# #import everythn from the math module
# from math import *
# print(sqrt(25))

#returns a sorted name list depending on the name  space
#helps devs explore the list of functions of a modulle on runtime
#print("List of functions:\n", dir(str), end="") #end tells the list to append a comma after every function
#usefull for string manipulation

#provides a portable way to interact with the operating system
# import os
# cwd = os.getcwd()
# print(cwd)

# files_and_dirs = os.listdir(cwd)
# print(files_and_dirs)

#json module helps us encode and decode python data structures into json objects
#encoding and decoding can be used in data serialization
import json
data = {
    "name": "Fes",
    "age": "24",
    "city": "Nairobi"
}
#encoding
json_data = json.dumps(data)
print(json_data)

#decoding
dec_json = json.loads(json_data)

#read on os.chmod os.chown

import math_operations

result_add = math_operations.add(5,3)
print(result_add)

#magic command %%writefile name.py
#floor division
print(11 // 2)
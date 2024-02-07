
# def convert_temperature(temperature,unit):
#     if unit == "C":
#         return (temperature * 9/5) + 32
#     elif unit == "F":
#         return  (temperature - 32) * 5/9
#     else:
#         raise ValueError("Invalid entry")
    
# fah_convertor = print(convert_temperature(20,"C"))
# cel_convertor = print(convert_temperature(20,"F"))
    
# Fahrenheit = "F"
# Celcius = "C"
# def convert_temperature(temperature,unit):
#     if unit == Celcius:
#         return (temperature * 9/5) + 32
#     elif unit == Fahrenheit:
#         return  (temperature - 32) * 5/9
#     else:
#         raise ValueError("Invalid entry")

# fah_convertor = print("{}{}".format(convert_temperature(20,"C"),"F"))
# cel_convertor = print("{}{}".format(convert_temperature(68,"F"),"C"))

def is_palindrome(text):
        rev_text = text[::-1]
        if rev_text == text:
            return True
        else:
            return False
        
print(is_palindrome("racecar"))

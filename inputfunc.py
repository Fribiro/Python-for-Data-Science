#functions
def add_numbers(a,b):
    result = a+b
    return result

sum_result = add_numbers(5,3)
# print(sum_result)

#docstring functions
#used to document functioncs, classes or modules
def my_function(parameters):
    '''
    this is a docstring
    it explains what the function does
    '''

def allowed_to_drive(age):
    if age >= 21:
        return True
    else:
        return False
    
# print(allowed_to_drive(42))
# print(allowed_to_drive(12))

def is_laundry_day(today, laundry_day = "Monday", on_vacation = False):
    if  today is laundry_day and today is not "Sunday" and on_vacation is False:
        return True
    else:
        return False
    
print(is_laundry_day("Monday"))
print(is_laundry_day("Wednesday", "Tuesday"))
print(is_laundry_day("Tuesday", "Tuesday", True))
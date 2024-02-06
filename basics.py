Age = 18
pi = 3.14

print(type(Age))
print(type(pi))
print(type(Age + pi))

multiline_str = '''
one
per 
line
'''
print(multiline_str)

#escaping characters
escape_str = "I said:\"python is great\""
print(escape_str)

#concatenation
one = "Code3"
two = "Camp"
print(one + "" + two)

#interpolation
first_name = "Festus"
last_name = "Ribiro"
greet = f"Hi {first_name} {last_name}"
print(greet)

#extracting substrings
name = "Duncan Ndegwa"
print(name[6:9]) #nd

Name = "Monty Python"
print(Name[6:]) #Python
print(Name[:5]) #Monty

#boolean
a = True
b = False
if a is True and b is False:
    print("Yaay")

#list - a collection of things
#stored in [] and are mutable
#list can store multiple and any datatype
list: [1,2,3,4,5]
multiple_types = [True,3.7, "Python", 15]
favourite_foods = ["Pasta", "Pizza", "Frenchfries"]
print(favourite_foods[1])

favourite_foods[0] = "Rosti"
print(favourite_foods)

#subsets of lists
print(favourite_foods[1:3])

#append list - add to the end of the list
fvourite_foods = ["Pasta", "Pizza", "Frenchfries"]
fvourite_foods.append("Paella")
print(fvourite_foods)

#insert() adds an item at a particular position
fvourite_foods.insert(1, "Soup")
print(fvourite_foods)

#remove item in a list
fvourite_foods.remove("Soup")
print(fvourite_foods)

favourite_drinks = ["water", "wine", "juice"]
favourites = [favourite_foods, favourite_drinks]
print(favourites)

print(favourites[1][1])

#list comprehension - 
fruits = ["apple","orange","banana"]
new_fruits = [fruit.upper() for fruit in fruits]
print(new_fruits)

#Tuple - an ordered collection of items
#enclosed in () and are immutable
new_tuple = ("a","b","c","d","e","f","g")
print(len(new_tuple))
print(new_tuple[1])
print(new_tuple[1:4])
print(new_tuple[:3])

#new_tuple[1] = "z"

#dictionaries - represent key values pairs enclosed in curly braces
language_creators = {
    "python": "Guido Van Rossum",
    "c": "Dennis",
    "java": "James",
    "Go": "Robert",
    "Perl": "Larry"
}

print(language_creators["python"])
print(len(language_creators))

#delete lang from dictionary
del(language_creators["Perl"])
print(language_creators)

#to view keys only
print(language_creators.keys)

#set - are unordered
fruits1 = {"apple","banana","cherry"}
fruits2 = {"banana","orange","pineapple"}

#discard
fruits1.discard("banana")
print(fruits1)

#pop can be used in retrieving arbitrary elements in a set
item = fruits1.pop()
print(item)
print(fruits1)

all_fruits = fruits1.union(fruits2)
print(all_fruits)


#conditional statements
#if, elif, else
age = 70
if age < 18: 
    print("You're a minor")
elif age >= 18 and age < 65:
    print("You're an adult")
else:
    print("You're a senior citizen")

#control stt(break, continue, pass)
numbers = [1,2,3,4,5]
for num in numbers:
    if num == 3:
        break #terminates the iteration when num is 3
    elif num == 2:
        continue #skips the iteration when num is 2
    print(num)

#pass is a null operation meaning it does nothing
for num in numbers:
    if num == 3:
        break #terminates the iteration when num is 3
    elif num == 2:
        pass 
    print(num)
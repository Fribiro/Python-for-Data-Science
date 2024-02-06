#write into a file
file = open("data.txt", "w")
file.write("Hello world")
file.close()

#use append to add text into a file
file = open("data.txt", "a")
file.write("\nWelcome to python")
file.write("\nLearning Ds")
file.close()
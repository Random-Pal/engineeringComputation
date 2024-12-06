import os
file = open("C:/Users/ALL E/Documents/my_file.txt", "w")
file.write("I am an Engineer\n")
file.write("Coding in Python is fun\n")
file.close()
file = open("C:/Users/ALL E/Documents/my_file.txt","r")
print(file.read())
##os.remove("C:/Users/ALL E/Documents/my_file.txt")
file = open("C:/Users/ALL E/Documents/my_file.txt","a")
file.write("My name is Alejandro\n")
file.close()
file = open("C:/Users/ALL E/Documents/my_file.txt" , "r")
print(file.read())
file.close()
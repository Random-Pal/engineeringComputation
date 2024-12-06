import os
with open("C:/Users/ALL E/Documents/newfile.txt","w") as file:
    file.write("PLEASE WORK\n")
with open("C:/Users/ALL E/Documents/newfile.txt", "a") as file:
    file.write("LET'S GOOOO")
with open("C:/Users/ALL E/Documents/newfile.txt" , "r") as file:
    print(file.read())
os.remove("C:/Users/ALL E/Documents/newfile.txt")
import os
if os.path.exists("C:/Users/ALL E/Documents/learn.txt"):
    os.remove("learn.txt")
else:
    print("The file does not exist.")
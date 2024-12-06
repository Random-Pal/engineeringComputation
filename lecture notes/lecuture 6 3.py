list1 = ["I am", "You are"]
list2 = ["health", "fine", "geek"]

list2Size = len(list2)

for item in list1:
    print("start outer for loop")
    i = 0
    while(i < list2Size):
        print(item,list2[i])
        i = i + 1
    print("end of for loop")
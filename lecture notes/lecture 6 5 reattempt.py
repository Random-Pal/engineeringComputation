#i = 5

##while i <= 5:
##    print("i")
##    i = i - 1
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print(j, end="")
        j = j -1
    i+=1
    print()
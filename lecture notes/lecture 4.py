farenheight = float(input("What is the farenheight to be converted? "))
c = 0

def celsius(x):
    x = 5/9*(farenheight-32)
    return x

celsius(farenheight)

print(celsius(farenheight))
import numpy as py

weekReadings = py.array([28.5,29.0,30.2,31.7,32.4,29.9,27.8])
toFarenheight = (weekReadings * 9/5) + 32
print("readings in F are", toFarenheight)
print("max f is ",max(toFarenheight))
print("min f is", min(toFarenheight))
print("mean is", py.mean(toFarenheight))
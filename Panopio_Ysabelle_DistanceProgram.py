#Programmer: Ysabelle D. Panopio
#Date: 08/18/2026
import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
d = math.sqrt((math.pow((x1-x2), 2)+(math.pow((y1-y2), 2))))
print(f"The distance between the two points is: {d}")

#Reflection:
#Math libraries helped simply my program by simplifying otherwise complicated code into only a few operations.
#The library helped simplify the process of calculating the distance by densifying the operations.
#Without sqrt() and pow() I'd be forced to calculate the distance using only what python has on it's own, addition, subtraction, division, etc.
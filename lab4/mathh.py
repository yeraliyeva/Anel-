#1 method convert degree to radian
import math 
degree = int ( input ( "Input degree: "))
rad = math.radians(degree)
print (rad)

# #1.1 method
import math
def rad(degree):
    print ( degree * (math.pi/180))
degree = int (input ("Input degree: "))
rad(degree)


#2 area of trapezoid
import math 
def trapi():
    print ( "Expected Output: ", 1/2 * (heig * (first_v + second_v)))
heig = int (input ("Height: "))
first_v = int (input ("Base, first value: "))
second_v = int (input ("Base, second value: "))
trapi()

#3 area of regular polygon
import math 
def area (n , s):
    print ( "The area of the polygon is: " , round((n * s ** 2) / (4 * math.tan(math.pi / n))))
n = int ( input ("Input number of sides: "))
s = int ( input ("Input the length of a side "))
area(n , s)


#4 area of a parallelogram
import math 
def area(a ,b):
    print ("Expected Output: ", a * b)
a = int (input ("Length of base: "))
b = int (input ("Height of parallelogram: "))
area(a,b)





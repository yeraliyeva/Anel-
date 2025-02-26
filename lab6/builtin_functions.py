#1)Write a Python program with builtin function to multiply all the numbers in a list
import math 
def multip(numbers):
    return math.prod(numbers)

nums = [2,3,4,5,6,7]
print(multip(nums))


#2)Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters
def main():
    string = input("Write your srting: ")
    upp_count = sum (1 for c in string if c.isupper())
    low_count = sum (1 for c in string if c.islower())
    print("Upperase:" ,upp_count , "\nLowercase:" ,low_count)

main()

#3) string is palindrome or not
def pal(s):
    return s == s[::-1]
str = input("Your word:")
print (pal(str))

#4)Write a Python program that invoke square root function after specific milliseconds
import time
def square(number, millisec):
    time.sleep(millisec / 1000)
    return f"Square root of {number} after {millisec} milliseconds is {pow(number , 0.5)}"

number = int(input("Enter a nunber: "))
millisec = int(input("Enter milliseconds: "))
print(square(number , millisec))

#5)that returns True if all elements of the tuple are true.
from functools import reduce 
from operator import mul
import time
import math 
def true(elements):
    return all(elements)
print(true((True , True , True)))
print(true((True, False, True)))










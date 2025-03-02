import functools

def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

nums = [1, 2, 3, 4, 5]
result = multiply_list(nums)
print("Product of numbers:", result)

#Write a Python program with builtin function that accepts a string and 
#calculate the number of upper case letters and lower case letters


def main():
    string = input("Write your string: ")
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    print("Lowercase:", lower_count)
    print("Uppercase:", upper_count)


if __name__ == "__main__":
    main()



#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

my_input_string = input()
reversed_string = ''.join(reversed(my_input_string))
print(my_input_string == reversed_string)




import time

number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))
time.sleep(milliseconds / 1000)

print("Square root of", number,  "after", milliseconds, "milliseconds is", pow(number, 0.5))




from functools import reduce
from operator import mul
import time
import math
def true(elements):
    return all(elements)

print(true((True, True, True)))
print(true((True, False, True)))
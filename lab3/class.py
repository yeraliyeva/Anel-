
#ex1
class string():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

x = string()
x.get_string()
x.print_string()

#ex2
class Shape:
    def __init__ (self):
        self.area = 0

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
shape = Shape()
print(shape.area)

square = Square(30)
print(square.area()) 

#ex3
class Shape:
    def __init__(self):
        pass

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
#ex4
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}  y={self.y}')

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
    

p1 = Point(2, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

p1.move(3, 6)
p1.show()

print(f'dist: {p1.dist(p2)}')

#ex5
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, count):
        self.balance += count

    def withdraw(self, count):
        if count > self.balance:
            print("Not enough money")
        else:
            self.balance -= count

user = Account(1000)
print(user.balance)
user.deposit(100)
print(user.balance)
user.withdraw(1200)
user.withdraw(100)
print(user.balance)

#ex6
class Filter:
    def __init__(self, num):
        self.num = num

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def primes(self):
        return list(filter(lambda x: self.is_prime(x), self.num))

num = [1, 2, 3, 4, 5, 6]
prime_filter = Filter(num)
prime_numbers = prime_filter.primes()

print("Prime numbers:", prime_numbers)

        
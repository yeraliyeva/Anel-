# class Daria:
#     def __init__(self):
#         pass
#     def areaa(self,rost,ves):
#         self.rost = rost
#         self.ves = ves
#         return rost * ves
# d=Daria()
# print(d.areaa(154, 43))

# class Anel(Daria):
#     def __init__(self):
#         pass
# a = Anel()
# print(a.areaa(176,98))

# class Assel(Anel):
#     def __init__(self):
#         pass
# s = Assel()
# print(s.areaa(186,43))


class Shape:
    def __init__(self):
        pass
    def area(self,len):
        self.len= len 
        print(self.len ** 3)

class Cube(Shape):
    def __init__(self,len):
        self.len = len
    def volume(self):
        pass
     
cube = Cube(5)
cube.area(5)



        


#isprime через while
# def isprime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i < n:
#         if n % i == 0:
#             i += 1
#             return False
#         else:
#             i += 1
#             return True
        
# def filter_prime(num): 
#     return[ n for n in num if isprime(n)]
# print(filter_prime([3, 4, 5, 6, 7, 8, 9]))

# def filter(num)
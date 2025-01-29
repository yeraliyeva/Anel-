# 1)Create a function to convert grams to ounces. 
def gramm(number):
    ounces = number * 28.3495231
    return ounces
print(gramm(int(input())))

# 2)takes temperature in Fahrenheit and converts it to Celsius
def temp(ff):
    celsius = (5 /9) * (ff-32)
    return celsius
print(temp(int(input())))

# 3)How many rabbits and how many chickens do we have?
def many(numhead, numleg):
    rabb = (numleg - 2 * numhead) // 2
    chickenn = numhead - rabb
    return rabb, chickenn
rabb = int(input())
chickenn = int(input())
print(many(rabb,chickenn))

# 4)prime numbers
def isprime(n):
    if n < 2 :
        return False
    for i in range(2, int(n)):
        if n % i ==0:
            return False
    return True
def filter_prime(num): 
    return[ n for n in num if isprime(n)]
print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9]))

#5)Write a function that accepts string from user and print all permutations of that string.
def perm(s, step=0):
    if step == len(s):  
        print("".join(s))
    else:
        for i in range(step, len(s)):
            s_list = list(s)  
            s_list[step], s_list[i] = s_list[i], s_list[step]  
            perm(s_list, step + 1)  
print(perm(input()))

#6)Write a function that accepts string from user, return a sentence with the words reversed.
def inverse(word):
    return " ".join(word.split()[::-1])  
print(inverse(input()))  

#7)Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        i += 1
    return False
numbeers = input()
nums = numbeers.split()
nums = [int(num) for num in nums]
print(has_33(nums))

#8)Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(anel):
    i = 0
    while i < len(anel)-2:
        if anel[i] == 0 and anel[i+1] == 0 and anel[i+2] == 7: 
            return True
        i += 1
    return False
daria = input()
anel = daria.split()
anel = [int(num) for num in anel]
print(spy_game(anel))











# 1)Create a function to convert grams to ounces. 
def gramm(number):
    ounces = number * 28.3495231
    return ounces


# 2)takes temperature in Fahrenheit and converts it to Celsius
def temp(ff):
    celsius = (5 /9) * (ff-32)
    return celsius


# 3)How many rabbits and how many chickens do we have?
def many(numhead, numleg):
    rabb = (numleg - 2 * numhead) // 2
    chickenn = numhead - rabb
    return rabb, chickenn



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


#5)Write a function that accepts string from user and print all permutations of that string.
def new_strings(s):
    if len(s)==1:
        return [s]
    new=[]
    for i in range(len(s)):
        for x in new_strings(s[:i]+s[i+1:]):
            new.append(s[i]+x)
    return new


#6)Write a function that accepts string from user, return a sentence with the words reversed.
def inverse(word):
    txt = word.split()
    return txt[::-1] 
 

#7)Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        i += 1
    return False
numbeers = [45,76,3,3,43,23]
# nums = numbeers.split()
# nums = [int(num) for num in nums]


#8)Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(anel):
    i = 0
    while i < len(anel)-2:
        if anel[i] == 0 and anel[i+1] == 0 and anel[i+2] == 7: 
            return True
        i += 1
    return False
daria = [1,2,34,45,0,0,7,87]
# anel = daria.split()
# anel = [int(num) for num in anel]


#9) Write a function that computes the volume of a sphere given its radius
def volume(san):
    vol = 0
    vol = (4/3)*math.pi*r**3
    return vol


#10)unique elements 
def uni(clovo):
    new_list = []
    i = 0
    while i < len(clovo):
        tf = True
        j = 0
        while j < i:
            if clovo[i]== clovo[j]:
                tf = False
            j += 1
        if tf:
            new_list.append(clovo[i])
        i += 1
    return new_list


#11)palindrom
def pal(p):
    clov = p[::-1]
    if clov == p:
        return True
    else:
        return False


#12)histogram
def histogram(daria):
    for i in daria:
        print('*'*i)


#13) guess number
import random
def gus():
    numm = random.randint(1,20)
    print("Hello! What is your name?")
    name = input()
    print("Well," , name , ", I am thinking of a number between 1 and 20.Take a guess.")
    chet = 0
    while True:
        n = int(input())
        if n<numm:
            print("Your guess is too low. Take a guess")
            chet+=1
        elif n>numm:
            print("Your guess is too high.Take a guess")
            chet+=1
        elif n==numm:
            print("Good job, " , name, "! You guessed my number in" , chet , "guesses!")
            break




















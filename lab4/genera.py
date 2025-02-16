#1
import math
def gen(n):
    cnt=2
    for i in range(1,int(math.sqrt(n))+1):
        yield i**cnt
       
rt=gen(49)
for i in rt:
    print(i)
#2
def EvenNum(n):
    p=[]
    for i in range(n+1):
        if i%2==0:
            p.append(i)
    yield p
y=EvenNum(int(input("num: ")))
for i in y:
    print(" ,".join(map(str,i)))
#3
def fourand(n):
    u=[]
    for i in range(n+1):
        if i%3==0 and i%4==0:
            u.append(i)
    yield u
r=fourand(int(input("write a num: ")))
for i in r:
    print(" ,".join(map(str,i)))
#4
def gt(a,b):
    you=[]
    for i in range(a,b+1):
        you.append(math.pow(i,2))
    yield you

a=int(input("start: "))
b=int(input("end: "))
ft=gt(a,b)
for i in ft:
    print(" ,".join(map(str,i)))
#5
def rat(n):
    op=[]
    for i in range(n,-1,-1):
        op.append(i)
    yield op
hey=rat(int(input("num: ")))
for i in hey:
    print(" ,".join(map(str,i)))
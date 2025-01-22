thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)



      

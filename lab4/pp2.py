import json
with open("example.json" , "r") as json_file:
    a = json.load(json_file)

json.dumps(data)



data = {"name" : "Alice", "age": 25 , "city": "New York"}
a = data
dict_to_json(data)

with open("example.json" , "w") as json_file:
    json.dump(json_file)
import math

# def gt(a,b):
#     you = []
#     for i in range(a,b+1):
#         you.append(math.pow(i,2))
#     yield you

# a = int(input())
# b = int(input())
# ft = gt(a,b)
# ft = map(str(a,b))
# for i in ft:
#     print(" ,".join(map(str,i)))
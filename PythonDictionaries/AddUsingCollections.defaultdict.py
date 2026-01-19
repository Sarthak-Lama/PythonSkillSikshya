from collections import defaultdict

d = defaultdict(int)
d["a"]+=1
print(d)

d=defaultdict(list)
d["b"].append(1)
print(d)

def deafult_value():
    return "N/A"

d = defaultdict(deafult_value)
print(d["c"])
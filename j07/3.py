d = {"apple" : ["سیب", "مردمک چشم", "کمپانی اپل"], "einfach" : ["آسان", "کویر"], "water" : "آب"}

# print(d.keys())
# print(d.values())
# print(d.items())

e = d.fromkeys(["apple", "banana", "cherry"], ["سیب", "مردمک چشم", "کمپانی اپل"])
print(d)

d.update({"apple" : ["سیب", "مردمک چشم", "کمپانی اپل", "زمین"]})
print(d)

g = d.get("apple")
g = d["apple"]

d.pop("apple")
d.popitem()
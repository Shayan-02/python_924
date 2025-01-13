d = {"apple" : ["سیب", "مردمک چشم", "کمپانی اپل"], "einfach" : ["آسان", "کویر"]}

for _ in d.values():
    for x in _:
        print(x, end=" ")
    print()

d["apple"].append("زمین")

for _ in d.values():
    for x in _:
        print(x, end=" ")
    print()

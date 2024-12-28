a = "hello world"
for _ in a:
    if _ == " ":
        a = a.replace(" ", "_")
    if _ == "o":
        _ = _.upper()
    print(_, end="")
print()
print(a)
# a = input().split()
# k = list(map(int, a))
# print(sum(k))

# l = []
# for i in a:
#     l.append(int(i))
# sum = 0
# for i in l:
#     sum += i
# print(sum)

li = [-1, 1, 2, 3, 4]
li2 = []
for i in li:
    li2.append(i**2)
print(li2)

print([i**2 for i in li])

newli = set(map(lambda x: x**2, li))
print(newli)
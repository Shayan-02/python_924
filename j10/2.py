def separator(ls):
    l1=[]
    l2=[]
    for i in ls:
        if int(i) %2==0:
            l1.append(int(i))
        else:
            l2.append(int(i))
    return l1, l2


a = input().split()
print(seprator(a))

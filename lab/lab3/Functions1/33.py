def has_33(x):
    a = None
    for i in x:
        if a == i == 3:
            return True
        a = i
    return False
x = []
n = int(input())
for i in range(n):
    a= int(input())
    x.append(a)
print(has_33(x))



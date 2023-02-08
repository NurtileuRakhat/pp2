def unique_list(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return l
print(unique_list([1, 2, 3, 1, 2]))

string = input()
a = sum([1 for i in string if i.islower()])
b = sum([1 for k in string if k.isupper()])

print(f'Yhe number of lowercase letters is {a} and the number of upper case letters is {b}')
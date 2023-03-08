fileR = open("123.txt",'r')
c = 0
for i in fileR:
    c+=1
print(c)
fileR.close()
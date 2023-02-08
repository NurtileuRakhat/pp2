def Prime(num):
        if(num < 2):
            return False
        else:
            for i in range(2,num):
                if(num % i == 0):
                    return False
        return True
l = [1,2,3,4,5,6,7,8,9]
for i in l:
     if(Prime(i)==True):
        print(i)

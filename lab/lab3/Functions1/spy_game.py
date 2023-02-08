def spy_game(nums):
    count=0
    for i in nums:
        if(i==0 and count==0):
            count=1
        if(i==0 and count==1):
            count=2
        if(i==7 and count ==2):
            count =3
        if(count == 3):
            return True
    return False
x = []
n = int(input())
for i in range(n):
    a= int(input())
    x.append(a)
print(spy_game(x))



def solve(numheads,numlegs):
    for i in range(numheads):
        j=numheads-i
        if 4*j+ 2*i == numlegs:
            return i,j
print(solve(35,94))

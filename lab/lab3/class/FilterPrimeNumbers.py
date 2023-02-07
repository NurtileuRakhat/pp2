class filterPrime():
    def Prime(self, num):
        if(num < 2):
            return False
        else:
            for i in range(2,num):
                if(num % i == 0):
                    return False
        return True
    def Filter(self, listPrime):
        return filter(lambda x: self.Prime(x), listPrime)
l = []
for i in range(5):
    a = int(input())
    l.append(a)
p = filterPrime()
p1 = list(p.Filter(l))
print(p1)
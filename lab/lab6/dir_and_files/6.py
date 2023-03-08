import os
for i in range(26):
    f = open(f'{chr(i + 65)}.txt', 'w')
    f.close()
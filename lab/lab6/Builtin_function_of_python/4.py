from time import sleep
from math import sqrt
num = int(input())
time = int(input())
sleep(time/1000)
print(f'Square root of {0} after {1} miliseconds is {sqrt(num)}'.format(num,time))
import os
a = input()
path = '.'
if os.access(a, os.F_OK):
    os.remove(a)
    print("Done")
else:
    print("There is no such file")
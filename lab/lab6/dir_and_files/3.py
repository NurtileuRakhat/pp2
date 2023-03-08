import os
a = input()
path = '.'
if os.path.exists(a):
    print('Exists')
    print('Filename is', os.path.basename(a))
    print('Directory name is', os.path.dirname(a))
else:
    print("There is no such file")
# C:\Users\Nurtileu\Desktop\git
# Exists
# Filename is git
# Directory name is C:\Users\Nurtileu\Desktop
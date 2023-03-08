import os
a = input()

print('Existence:', os.access(a, os.F_OK)) # Существование
print('Readable:', os.access(a, os.R_OK)) # Читаемость
print('Writable:', os.access(a, os.W_OK)) # Возможность записи
print('Executable:', os.access(a, os.X_OK)) # Возможность выполнения
# C:\Users\Nurtileu\Desktop\s
# Existence: False
# Readable: False
# Writable: False
# Executable: False
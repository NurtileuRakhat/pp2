import os
path = r'C:\Users\Nurtileu\Desktop\git'
print("Only directories:", [imya for imya in os.listdir(path) if os.path.isdir(os.path.join(path, imya))])
print("Only files:", [imya for imya in os.listdir(path) if os.path.isfile(os.path.join(path, imya))])
print("All directories and files:", [imya for imya in os.listdir(path)])
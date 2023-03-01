import re
def program(string):
    return re.sub("[ ,.]", ":", string)
print(program("K B,T.U"))

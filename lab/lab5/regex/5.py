import re
def program(string):
    str = "a.+b$"
    if re.search(str, string):
        return f"Correct"
    else:
        return f"Incorrect"
print(program("aabbccccccc"))
print(program("asb"))
import re
def program(string):
    str = "ab{2,3}"
    if re.search(str, string):
        return f"Correct"
    else:
        return f"Incorrect"
print(program("aabbccccccc"))
print(program("aabbbbbbc"))
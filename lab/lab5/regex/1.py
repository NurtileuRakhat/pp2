import re
def ab(string):
    str = "^ab*$"
    if re.search(str, string):
        return f"Correct"
    else:
        return f"Incorrect"
print(ab("abc"))
print(ab("abbbbbb"))
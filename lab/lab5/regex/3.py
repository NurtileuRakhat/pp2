import re
def program(str):
    s = "^[a-z]+_[a-z]"
    if re.search(s,str):
        return f"Correct"
    else:
        return f"Incorrect"
print(program("aaaabbb_amkfam"))
print(program("aAAAa_aaBBa"))
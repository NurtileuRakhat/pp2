import re
def program(str):
    print(re.findall("[A-Z][a-z]*", str))
program("SsdHdd")
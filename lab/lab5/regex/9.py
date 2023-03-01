import re
def program(str):
    m = re.findall("[A-Z][a-z]*", str)
    print(' '.join(m))
program("KbtuPython")

import re
def program(str):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower())

program("KbtuUniversity")
import re

def oneUpper(text):          
        string = '[A-Z]+[a-z]+$'
        if re.search(string, text):
                return('Correct')
        else:
                return('Incorrect')
print(oneUpper("Kbtu"))

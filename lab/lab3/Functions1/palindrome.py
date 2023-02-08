def palindrome(string):
    copy = string
    if(string == copy[::-1]):
        return f"Palindrome"
    return f"Not palindrome"
s = input()
print(palindrome(s))
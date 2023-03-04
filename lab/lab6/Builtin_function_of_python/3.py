import itertools
s = input()
reverse_s = ''.join(reversed(s))
print("Palindrome") if s == reverse_s else print("Not Palindrome")
def reverse_words(s):
    return ' '.join(reversed(s.split()))
s = input()
print(reverse_words(s))
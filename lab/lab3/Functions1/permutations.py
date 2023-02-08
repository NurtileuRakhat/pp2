import itertools
s = input()
def permutations(s):
    return list(itertools.permutations(s))
print(permutations(s))
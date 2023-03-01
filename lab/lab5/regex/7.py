import re 
def p(str):
    d = []
    s =re.split("_",str)
    for i in s:
        d.append(i.capitalize())
    return d
print(''.join(p("k_b_t_u")))
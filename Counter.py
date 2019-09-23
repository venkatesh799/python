from collections import Counter
a={"a":2,"b":3,"c":1}
b={"a":1,"b":2,"c":2}
c=Counter(a)-Counter(b)
d=Counter(b)-Counter(a)
print(c)
print(d)


'''
OUTPUT:    Counter({'a': 1, 'b': 1})
           Counter({'c': 1})
           
'''

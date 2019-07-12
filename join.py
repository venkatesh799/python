l=[('hello','im','venkatesh'),('how','are','you')]
res=[' '.join(tups) for tups in l]
print(res)             #['hello im venkatesh', 'how are you']
res1=list(map(' '.join,l))
print(res1)              #['hello im venkatesh', 'how are you']

'''
zip() is used to map the similar index of multiple containers
'''
names=['A','B','C']
marks=[100,92,83]
roll=[1,1,1]
mapped=zip(names,marks,roll)
mapped=set(mapped)
print(mapped)                #{('C', 83, 1), ('A', 100, 1), ('B', 92, 1)}

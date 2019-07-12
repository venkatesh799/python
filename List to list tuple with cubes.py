# list to list of  tuple with cubes
l=[1,2,3]
l2=[(val,pow(val,3)) for val in l]
print(l2)  #[(1, 1), (2, 8), (3, 27)]

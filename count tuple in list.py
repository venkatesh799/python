'''
Count the elements in a list until an element is a Tuple
Input : [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
Output : 4

Input : [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]
Output : 1
'''

l=[1,3,4,(2,3,4,5),89,(5,4,4)]
count=0
for x in l:
    if isinstance(x,tuple):
        break
    count+=1
print(count)   # 3

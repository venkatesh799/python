from numpy import *
m=[]
r=int(input("Row"))
c=int(input("Col"))
for i in range(0,r):
    print("Enter {0} row Elements".format(i))
    a=[]
    for j in range(0,c):
        a.append(int(input()))
    m.append(a)
print(m)

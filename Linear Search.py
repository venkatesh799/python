# Linear Serach Using Python
#The time complexity of below algorithm is O(n).

l=[1,4,6,5,9,10,3,2]
target=10
flag=0
for x in range(len(l)):
    if target == l[x]:
        flag=1
        break
if flag ==1 :
    print("Target Found At Index :",x)
else:
    print("Target Not Found")

l1=[1,2,3]
l2=['a','b','c']
l3=[]
i,j=0,0
while i < len(l1) and j < len(l2):
    l3.append(l1[i])
    l3.append(l2[j])
    i=i+1
    j=j+1
while i < len(l1):
    l3.append(l1[i])
    i+=1
while j < len(l2):
    l3.append(l1[i])
    j+=1
print(l3)  # [1,'a',2,'b',3,'c']

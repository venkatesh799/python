s="v!en@ka#te*s%h"
l1=[]
l2=[]
l3=[]
i,j=0,0
# Seperating chars and Special Characters
for x in range(len(s)):
    if s[x].isalpha():
        l1.append(s[x])
    else:
        l2.append(s[x])
print(l1)   #['v', 'e', 'n', 'k', 'a', 't', 'e', 's', 'h']
print(l2)    # ['!', '@', '#', '*', '%']
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
print(l3)  #['v', '!', 'e', '@', 'n', '#', 'k', '*', 'a', '%', 't', 'e', 's', 'h']



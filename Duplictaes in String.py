s="hello world"
l=[]
for x in range(len(s)):
    if s[x] in s[x+1:] and s[x] not in l:
        l.append(s[x])
print(l)

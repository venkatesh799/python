s="Gee#ks$%For$Geeks@"
ch=[]
sp=[]
for x in range(len(s)):
    if s[x]>='a' and s[x]<='z' or s[x]>='A' and s[x]<='Z':
        ch.append(s[x])
    else:
        sp.append(s[x])
print(ch)
print(sp)

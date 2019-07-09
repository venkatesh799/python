s="Gee#ks$%For$Geeks@"
ch=[]
sp=[]
for x in range(len(s)):
    if s[x]>='a' and s[x]<='z' or s[x]>='A' and s[x]<='Z':  # we can use str.isalpha() also
        ch.append(s[x])
    else:
        sp.append(s[x])
print(ch)
print(sp)

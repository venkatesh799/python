s="hello world"
f={}
s=s.replace(" ","")
for x in range(len(s)):
    if s[x] in f:
        f[s[x]]=f[s[x]]+1 
    else:
        f[s[x]]=1
print(f)

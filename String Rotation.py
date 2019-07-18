''' String Rotation
Input :rhdt:246
output :trhd
Input :ghftd:1246
output:ftdgh
every String Associated with a number Seperated by semicolon, if sum of square of digit is even(2*2 + 4*4 + 6*6 =56[EVEN])
then rotate String by 1 position from right.(rhdt becomes trhd)
if sum of Squares of a digit is Odd(1*1 + 2*2 + 4*4 + 6*6 = 57 [ODD] then rotate string by 2 postions from left
(ghftd becomes ftdgh)  '''


s=input().strip()
l=s.split(":")  #seperating number and String
s_l=list(l[0])
n_l=list(l[1])
sum_s=0
for x in n_l:
    sum_s=sum_s+int(x) ** 2       # Sum of Squares of a Digit
if sum_s%2 ==0:
    new=s_l[len(s_l)-1]
    del s_l[len(s_l)-1]
    s_l.insert(0,new)
    print(str("".join(s_l)))
else:
    new=s_l[0:2]
    del s_l[0:2]
    ne=s_l+new
    print(str("".join(ne)))

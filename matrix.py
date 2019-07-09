from numpy import *
r=int(input("Row"))      # 3
c=int(input("Col"))       # 3
l=list(map(int,input().split()))    # 1 2 3 4 5 6 7 8 9
matrix=array(l).reshape(r,c)
print(matrix)

'''   [ [ 1 , 2, 3],
         [ 4 , 5, 6],
         [ 7 , 8, 9] ]  '''

        

#Given a matrix A, return the transpose of A.
#The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans=[[j*0 for j in range(len(A))] for i in  range(len(A[0]))]
        for x in range(len(A)):
            for y in range(len(A[0])):
                ans[y][x]=A[x][y]
        return ans

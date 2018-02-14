class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        A = [[0 for _ in range(rowIndex+1)] for _ in range(rowIndex+1)]
        for i in range(0,rowIndex+1):
            for j in range(0,i+1):
                if (i == j) or (j == 0):
                    A[i][j] = 1
                else:
                    A[i][j] = A[i-1][j-1] + A[i-1][j]
        
        return A[rowIndex]
        
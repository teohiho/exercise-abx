class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)==1:
            return True
        for x in range(len(matrix[0])-1):
            for y in range(len(matrix)-1):
                if matrix[y][x] != matrix[y+1][x+1]:
                    return False
        return True

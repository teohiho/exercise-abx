class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        
        if not M:
            return M
        for x in range(len(M)):
            for y in range(len(M[0])):
                ne = []
                for h in [-1,0,1]:
                    for c in [-1,0,1]:
                        if (0 <= (x + h) < len(M)) and (0 <= (y + c) < len(M[0])):
                            ne.append(M[x+h][y+c])
                res[x][y] = sum(ne) // len(ne)
        return res
            
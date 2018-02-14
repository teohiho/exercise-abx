class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        i = 1
        if n == 1 or n==0:
            return n
        while i <= n:
            a = a + i 
            if a <= n:
                i +=1
            else:
                return i-1
            
        
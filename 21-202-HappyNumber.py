class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 4:
            a = 0
            for i in range(len(str(n))):
                a = a + int(str(n)[i]) * int(str(n)[i])
            n = a
        return n == 1
    
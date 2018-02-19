class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        array = [1]
        for i in range(n):
            a = b
            array.append(a)
            b = array[i] + b
        return a
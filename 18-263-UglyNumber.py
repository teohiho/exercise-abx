class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        array = [2,3,5]
        if num <= 0:
            return False
        for x in array:
            while num % x == 0:
                num = num / x
        return num == 1
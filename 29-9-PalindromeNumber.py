class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        b = 0
        if len(str(x)) == 1:
            return True
        if x < 0:
            return False
        while temp != 0:
            b = b*10 + temp % 10
            temp //= 10
        return b == x
            
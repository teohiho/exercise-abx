class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        if num/10 < 1:
            return num
        while num:
            result += num % 10
            num //= 10
        return self.addDigits(result)
  

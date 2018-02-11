class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = num
        du = ""
        if num == 0: return '0'
        while abs(num):
            du = str(abs(num) % 7) + du
            num = abs(num) // 7
        if a < 0:
            return "-" + du
        else:
            return du
        
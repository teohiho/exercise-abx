class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit = bin(num)[2:]
        s = 0
        if len(bit) == 1:
            if bit == "0":
                s = 1
                return s
            else:
                s = 0
                return s
        for x,y in enumerate(bit[::-1]):
            if y == "0":
                s += 2 ** x
        return s
    
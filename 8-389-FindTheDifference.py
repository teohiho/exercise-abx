class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = 0
        for x in s:
            a = ord(x) + a
        for y in t:
            a = a - ord(y)
        return chr(-a)
        
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1, s2 = 0, 0
        for x in range(len(s)):
            s1 = ord(s[x]) - 64
            s2 = 26 * s2 + s1
        return s2
      
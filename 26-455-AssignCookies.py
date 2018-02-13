class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        res = 0
        i = 0
        for x in s:
            if i == len(g):
                break
            if x >= g[i]:
                res += 1
                i += 1
        return res
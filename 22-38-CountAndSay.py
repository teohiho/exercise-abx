class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            a = s[0]
            count = 0
            res = ''
            for x in s:
                if a == x:
                    count += 1
                else:
                    res += str(count) + a
                    a = x
                    count = 1
            res += str(count) + a
            s = res
        return s
            
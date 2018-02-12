class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = len(s)
        if a == 0:
            return True
        if a % 2 != 0:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        if s == '':
            return True
        else:
            return False
        
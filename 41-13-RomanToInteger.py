class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arrRoman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        # array = list(s)
        a = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            value = arrRoman[s[i]]
            if value >= a:
                res += value
            else:
                res -= value
            a = value
        return res
            
        
        
            
            
        
            
        
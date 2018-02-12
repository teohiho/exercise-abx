class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        array = ["A","L","P"]
        countA = 0
        for i,x in enumerate(s):
            if s[i] == array[0]:
                countA += 1
                if countA > 1:
                    return False
            elif i > 1 and s[i] == array[1] and i > 1 and s[i-1] == array[1] and s[i-2] == array[1]:
                    return False
        return True
        

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        array = []
        array = list(S.replace('-', ''))
        size = len(array)
        for i in range(size, 0, -K):
            if i != size:
                array.insert(i,'-')
        return ''.join(array).upper()

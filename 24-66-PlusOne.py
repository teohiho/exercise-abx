class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = int(''.join(map(str, digits)))
        a = a + 1
        array = []
        for x in str(a):
            array.append(int(x))
        return array
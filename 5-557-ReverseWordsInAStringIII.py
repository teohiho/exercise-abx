class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = []
        array = s.split(' ')
        # mang = [100]
        for x in range(len(array)):
            stack = []
            for y in array[x]:
                stack.append(y)
            stack.reverse();
            array[x] = ''.join(stack)
        return ' '.join(array)
        
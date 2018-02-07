class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for x in s:
            stack.append(x)
        stack.reverse();
        connect = ''
        return connect.join(stack)
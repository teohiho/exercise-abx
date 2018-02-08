class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def add(a, b):
            if b == 0:
                return a
            b1 = a ^ b
            b2 = a & b
            b3 = b2 << 1
            return add(b1, b3)
        if a*b < 0:
            if a > 0:
                return self.getSum(b,a)
            if -a == b:
                return 0
            if -a < b:
                return -add(-a, -b)
        return add(a, b)
        
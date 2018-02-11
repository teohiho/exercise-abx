class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = set(nums)
        a = 0
        b = 0
        for x in array:
            a += x
        for y in nums:
            b += y
        res = a * 2 - b
        return res
    
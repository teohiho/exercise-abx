class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        sumSet = sum(list(set(nums)))
        array.append(sum(nums)- sumSet)
        array.append( sum(range(1,len(nums)+1)) - sumSet)
        return array
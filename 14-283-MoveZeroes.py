class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        tmp = 0
        while i < len(nums):
            if nums[i] != 0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j+=1
            i+=1

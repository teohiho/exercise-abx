class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, x in enumerate(nums):
            if target == x:
                return i
            elif target < x:
                nums.insert(i, target)
                return i
            elif target > nums[len(nums)-1]:
                return len(nums)
                
        
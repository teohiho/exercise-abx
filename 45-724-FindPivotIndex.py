class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if not nums:
            return -1
        if size == 1 or (sum(nums)-nums[0] == 0):
            return 0
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]
        left[0] = nums[0]
        right[0] = nums[size-1]
        for i in range(1, size):
            left[i] = nums[i] + left[i-1]
            right[i] = nums[size-1-i] + right[i-1]
        for i in range(1, size):
            if left[i] == right[size-1-i]:
                return i
        return -1
        
#         if not nums:
#             return -1
#         if len(nums) == 1 or (sum(nums)-nums[0] == 0):
#             return 0
#         for i in range(1, len(nums)):
#             left = right = 0
#             for j in range(i-1, -1, -1):
#                 left += nums[j]
#             for k in range(i+1,len(nums)):
#                 right += nums[k]
            
#             if left == right:
#                 return i
#         return -1
        
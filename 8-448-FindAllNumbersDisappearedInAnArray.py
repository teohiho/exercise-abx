class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        nums.sort()
        nums.insert(0, 0)
        nums.append(len(nums))
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] > 1:
                r = nums[i - 1] + 1
                while r != nums[i]:
                    array.append(r)
                    r += 1
            i += 1
        return array
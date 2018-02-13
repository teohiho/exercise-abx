class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        array = {}
        for i, x in enumerate(nums):
            array[x] = i
        numsSort = sorted(nums)
        res = ["" for _ in range(len(nums))]
        for i, x in enumerate(numsSort[::-1]):
            if i == 0:
                res[array[x]] = "Gold Medal"
            elif i == 1:
                res[array[x]] = "Silver Medal"
            elif i == 2:
                res[array[x]] = "Bronze Medal"
            else:
                res[array[x]] = str(i + 1)
        return res
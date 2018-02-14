class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        b = 0
        
        for i in range(2,len(cost)+1):
            if b + cost[i-2] <= res + cost[i-1]:
                a = b + cost[i-2]
            else:
                a = res + cost[i-1]
            b = res
            res   = a
        return res
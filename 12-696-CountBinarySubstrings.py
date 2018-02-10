class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        result = []
        while w > 1:
            if area % w == 0:
                result.append(area // w)
                result.append(w)
                return result
            w -= 1
        result.append(area)
        result.append(1)
        return result
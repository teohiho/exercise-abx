class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        size1 = len(nums1)
        size2 = len(nums2)
        array = [0 for _ in range(size1)]
        for i in range(size1):
            for j in range(size2):
                if nums1[i] == nums2[j]:
                    array[i] = j
      
        for i in range(len(array)):
            cont = 0
            j = array[i]
            if j == size2 - 1:
                nums1[i]=-1
            else:
                while j != size2:
                    if nums1[i]< nums2[j]: 
                        nums1[i]=nums2[j]
                        cont = 1
                        break 
                    j += 1
                if cont == 0:
                    nums1[i] = -1
        return nums1

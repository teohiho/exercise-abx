# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stackP = []
        stackQ = []
        if p:
            stackP.append(p)
        if q:
            stackQ.append(q)
        while stackP and stackQ:
            curP = stackP.pop()
            curQ = stackQ.pop()
            if curP.val != curQ.val:
                return False
            if curP.left:
                stackP.append(curP.left)
            if curQ.left:
                stackQ.append(curQ.left)
            if len(stackP) != len(stackQ):
                return False
            if curP.right:
                stackP.append(curP.right)
            if curQ.right:
                stackQ.append(curQ.right)
            if len(stackP) != len(stackQ):
                return False
        return len(stackP) == len(stackQ)
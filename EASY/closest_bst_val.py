# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        c= root.val
        
        while root:
            if abs(root.val-target)<abs(c-target):
                c =root.val
            else:
                if root.val<target:
                    root = root.right
                else:
                    root = root.left
        return c
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        lt = self.minDepth(root.left)+1
        rt = self.minDepth(root.right)+1
        
        return rt if lt==1 else lt if rt==1 else min(lt,rt)
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            lft = self.maxDepth(root.left)
            rgt = self.maxDepth(root.right)
            return max(lft,rgt)+1
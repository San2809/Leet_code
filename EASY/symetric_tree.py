class Solution(object):
    def isSame(self,left,right):
        if not left and not right:
            return True
        elif left and right:
            if left.val !=right.val:
                return False
            return self.isSame(left.left,right.right) and self.isSame(left.right, right.left)
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSame(root.left, root.right)
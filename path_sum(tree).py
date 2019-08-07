class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        start = root.val
        if start == sum and root.left == None and root.right == None:
            return true
        return self.helper(root.left, root.right, start, sum)
    
    
    def helper(self,left, right, val, sum):
        if not left and right:
            if sum == val:
                return 1
            else:
                return 0
        sum_left, sum_right = 0,0
            
        if left:
            sum_left = self.helper(left.left, left.right, val+left.val, sum)
        if right:
            sum_right = self.helper(right.left, right.right, val+right.val, sum)
            
        return max(sum_left, sum_right)
            
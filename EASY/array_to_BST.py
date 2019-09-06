class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums ==[]:
            return None
        
        mid = len(nums)//2
        
        Tree = TreeNode(nums[mid])
        
        Tree.left= self.sortedArrayToBST(nums[:mid])
        Tree.right = self.sortedArrayToBST(nums[mid+1:])
        return Tree
        
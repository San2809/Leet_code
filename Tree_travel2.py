class Solution(object):
    def help(self,root,res,level):
        if root:
            if len(res)<=level:
                res.append([])
            res[level].append(root.val)
            self.help(root.left,res,level+1)
            self.help(root.right,res,level+1)
        return res[::-1]
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.help(root,[], 0)
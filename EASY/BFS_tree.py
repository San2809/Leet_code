    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr =[]
        h = self.height(root)
        for i in range(1,h+1):
            self.givenLevel(root,arr, i)
        return arr
        
        
    def givenLevel(self,root, arr, level):
        if root is None:
            return
        if level ==1:
            temp = []
            temp.append(root.val)
            arr.append(temp)
        elif level>1:
            self.givenLevel(root.left, arr, level-1)
            self.givenLevel(root.right, arr, level-1)
    
    def height(self,root):
        if root is None:
            return 0
        else:
            lht = self.height(root.left)
            rht = self.height(root.right)
            
        if lht>rht:
            return lht+1
        else: 
            return rht+1
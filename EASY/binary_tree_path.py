# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res =[]
        def construct_paths(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += "->"
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
                    
        construct_paths(root,'')
        return res
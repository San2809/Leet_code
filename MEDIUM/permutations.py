class Solution(object):
    def helper(self, nums, path, res):
        if len(nums)==len(path):
            res.append(path)
            return
        else:
            for i in nums:
                if i not in path:
                    self.helper(nums, path+[i], res)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        self.helper(nums, [], res)
        return res
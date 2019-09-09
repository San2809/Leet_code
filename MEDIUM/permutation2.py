class Solution(object):
    
    def permuteUnique(self, nums):
        nums.sort()
        res = list()
        def bfs(nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    bfs(nums[:i]+nums[i+1:], [nums[i]]+path)            
        bfs(nums)
        return res
        
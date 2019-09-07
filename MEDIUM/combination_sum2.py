class Solution(object):
    def helper(self, nums, target, index,path, ans):
        
        if target < 0:
            return None
        if target ==0 and(path not in ans):
            ans.append(path)
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.helper(nums, target-nums[i], i+1, path+[nums[i]], ans)
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans =[]
        candidates.sort()
        self.helper(candidates, target, 0, [], ans)
        return ans
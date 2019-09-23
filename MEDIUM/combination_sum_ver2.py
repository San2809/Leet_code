class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, 0, [], res)
        return res
    
    def dfs(self, candidates, target, pos, curSum, curList, res):        
        if curSum == target:
            res.append(curList)
            return
        for i in range(pos, len(candidates)):
            num = 1
            while curSum + num * candidates[i] <= target: 
                self.dfs(candidates, target, i + 1, curSum + num * candidates[i], curList + num * [candidates[i]], res)
                num += 1
        
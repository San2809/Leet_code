class Solution(object):
    def combinationSumDP(self, candidates, target):
        dp = {}
        dp[0] = [[]]
        candidates.sort()
        for c in candidates:
            for t in range(c, target + 1):
                if (t-c) in dp:
                    if t not in dp:
                        dp[t] = []
                    for comb_t_m_c in dp[t-c]:
                        dp[t].append(comb_t_m_c + [c])
        return dp[target] if target in dp else []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSumDP(candidates, target)
        
        
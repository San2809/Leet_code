class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not k or not n:
            return 0
        dp = [0,k]
        
        for i in range(1,n):
            dp =[dp[1], sum(dp)*(k-1)]
        return sum(dp)
        
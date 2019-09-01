class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, 1]
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[-1]
        
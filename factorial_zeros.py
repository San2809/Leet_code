class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        divisor = 5
        cnt =0 
        while (math.floor(n/divisor)!=0):
            cnt += math.floor(n/divisor)
            divisor *= 5
        return int(cnt)
        
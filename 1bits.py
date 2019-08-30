class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 0
        while n >0:
            t += n&1
            n >>= 1
        print(n)
        return t
        
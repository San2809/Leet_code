class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n%2 ==0 and n>1:
            n /=2
        return n==1
        
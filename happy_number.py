class Solution(object):
    def helper(self,n):
        res =0
        while n:
            a = n%10
            n = n//10
            res +=a**2
        return res
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([n])
        while n != 1:
            n = self.helper(n)
            if n in s:
                return False
            else:
                s.add(n)
        return True
            
            
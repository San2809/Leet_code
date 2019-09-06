class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while(n>0):
            d= n%26
            if d==0:
                res = 'Z'+res
                d = 26
            else:
                res = chr(d+64)+res
            n = (n-d)/26
        return res
        
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        l = len(s)
        res = 0
        while l>0:
            for i in s:
                res += (letters.index(i)+1)*26**(l-1)
                l -= 1
        return res
    
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        while num>0:
            num -=n
            n +=2
        return num == 0
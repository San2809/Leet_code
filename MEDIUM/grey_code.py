class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans =[0]
        for i in range(n):
            temp = ans[:]
            temp.reverse()
            next_part = [j+2**i for j in temp]
            ans +=next_part
        return ans
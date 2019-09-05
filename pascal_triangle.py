class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        
        for j in range(numRows-1):
            prev = res[-1]
            new = [1]+[prev[i]+prev[i+1] for i in range(j)]+[1]
            res.append(new)
        return res
        
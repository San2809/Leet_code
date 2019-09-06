from collections import defaultdict
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows<=0:
            return s
        res = [[] for _ in range(numRows)]
        curr =0
        isDown = True
        
        for i in range(len(s)):
            res[curr].append(s[i])
            
            if curr >=numRows-1:
                isDown =False
            elif curr<=0:
                isDown = True
            
            if isDown:
                curr +=1
            else:
                curr -=1
        return "".join(["".join(char) for char in res])
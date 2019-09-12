class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <2:
            return s
        ans = ["" for i in range(numRows)]
        num =0
        flag =True
        for char in s:
            ans[num] +=char
            
            if num == numRows-1:
                flag =False
            
            if not flag and num==0:
                flag = True
            num +=1 if flag else -1
        return "".join(ans)
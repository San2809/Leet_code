class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res =[]
        def helper(arr, s,i,j):
            if i==n:
                arr.append(s+")"*(n-j))
                return
            helper(arr,s+"(",i+1,j)
            if j<i:
                helper(arr, s+")",i,j+1)
        helper(res,"(",1,0)
        return res
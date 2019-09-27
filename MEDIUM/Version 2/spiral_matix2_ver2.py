class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        r1 = 0
        res=[]
        r2 = len(matrix)
        c1 = 0
        c2 = len(matrix[0])
        
        while r2>r1 and c2>c1:
            for i in range(c1, c2):
                res.append(matrix[r1][i])
            for j in range(r1+1, r2-1):
                res.append(matrix[j][c2-1])
            
            if r2 != r1+1:
                for i in range(c2-1, c1-1, -1):
                    res.append(matrix[r2-1][i])
            if c1 != c2-1:
                for j in range(r2-2, r1, -1):
                    res.append(matrix[j][c1])
            r1 +=1
            r2-=1
            c1+=1
            c2-=1
        return res
        
        
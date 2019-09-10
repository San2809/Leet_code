class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row , col = set(), set()
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for i in range(row_len):
            for j in range(col_len):
                if i in row or j in col:
                    
                    matrix[i][j] = 0
    
        
        
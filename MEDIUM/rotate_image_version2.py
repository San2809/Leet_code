class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp =[]
        k=0
        for i in range(len(matrix)):
            for j in range(n):
                temp.append(matrix[n-j-1][i])
                
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[k]
                k +=1
            
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0] :
            return False
        start = 0
        end =len(matrix)-1
        while start <=end:
            mid = (start+end)//2
            
            while not matrix[mid]:
                if mid <=end:
                    mid +=1
                elif mid>=start:
                    mid -=1
                else:
                    return False
            if target >= matrix[mid][0]:
                if target in matrix[mid]:
                    return True
                start = mid+1
            else:
                end = mid-1
        return False
                    
        
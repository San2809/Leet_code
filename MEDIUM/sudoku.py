class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num =int(num)
                    box_idx = (i//3)*3 + j//3
                
                    row[i][num] = row[i].get(num,0)+1
                    col[j][num] = col[j].get(num,0)+1
                    boxes[box_idx][num] = boxes[box_idx].get(num,0)+1
                
                    if row[i][num]>1 or col[j][num]>1 or boxes[box_idx][num]>1:
                        return False
        return True
        
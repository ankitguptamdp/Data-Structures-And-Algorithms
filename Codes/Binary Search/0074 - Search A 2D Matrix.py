class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS-1
        while top<=bottom:
            row = (top+bottom)//2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if top > bottom:
            return False

        left, right = 0, COLUMNS-1
        row = (top+bottom)//2
        while left <= right:
            column = (left+right)//2
            if target < matrix[row][column]:
                right = column - 1
            elif target > matrix[row][column]:
                left = column + 1
            else:
                return True
        return False
        
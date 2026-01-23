class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = 0
        c = len(matrix[0])-1

        nr = len(matrix)-1
        nc = len(matrix[0])-1

        while 0 <= r <= nr and c >= 0:
            print(r,c)
            print(matrix[r][c])
            if matrix[r][c] == target:
                return True

            elif matrix[r][c] > target:
                c -= 1
                
            else:
                r += 1
            
            
                

        if 0 <= r <= nr and c >= 0 and matrix[r][c] == target:
            return True

        else:
            return False
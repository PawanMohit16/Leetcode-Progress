class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix) - 1
        col = len(matrix[0]) - 1 

        key = (row + 1) * (col + 1)
        cnt = 0

        t = 0
        r = col
        b = row
        l = 0

        ans = []

        while cnt < key:
            for i in range(l, r + 1):
                if cnt >= key: break
                ans.append(matrix[t][i])
                cnt += 1

            t += 1


            for i in range(t, b + 1):
                if cnt >= key: break
                ans.append(matrix[i][r])
                cnt += 1

            r -= 1
            
            for i in range(r, l - 1, -1):
                if cnt >= key: break
                ans.append(matrix[b][i])
                cnt += 1


            b -= 1

            for i in range(b, t - 1, -1):
                if cnt >= key: break
                ans.append(matrix[i][l])
                cnt += 1

            l += 1

        return ans

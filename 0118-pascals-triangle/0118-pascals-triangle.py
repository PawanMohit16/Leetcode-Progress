class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        arr = []
        
        for i in range(n-1,-1,-1):
            temp = []
            for j in range(i, n):
                temp.append(1)

            arr.append(temp)

        for i in range(2, n):
            for j in range(1, len(arr[i-1])):
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

        return arr

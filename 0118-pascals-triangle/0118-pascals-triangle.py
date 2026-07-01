class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        arr = []
        
        for i in range(n-1,-1,-1):
            temp = []
            for j in range(i, n):
                temp.append(1)

            arr.append(temp)

        if n > 2:
            for i in range(2, n):
                print(len(arr[i]))
                for j in range(len(arr[i-1])-1):
                    arr[i][j+1] = arr[i-1][j]+arr[i-1][j+1]



        return arr

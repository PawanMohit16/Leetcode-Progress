class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []

        for i in range(1, numRows + 1):
        
            insider = [1] * i
            for j in range(1, i-1):
                insider[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(insider)

        return ans
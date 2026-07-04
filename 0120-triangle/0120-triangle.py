class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = []
        for i in range(1, n+1):
            dp.append([0] * i)

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        print(dp)

        minie = float('inf')

        for i in range(n):
            minie = min(minie, dp[-1][i])

        return minie


        
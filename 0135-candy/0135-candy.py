class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n
        next = 1

        for i in range(n-1):

            if ratings[i] < ratings[next]:
                ans[next] = ans[i]+1

            next += 1

        next = n - 2

        for i in range(n-1,0,-1):

            if ratings[next] > ratings[i]:
                ans[next] = max(ans[next], ans[i]+1)

            next -= 1

        print(ans)
        return(sum(ans))
            
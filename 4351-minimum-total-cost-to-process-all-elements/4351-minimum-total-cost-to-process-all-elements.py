class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        cost = 0
        ans = k

        for num in nums:
            if ans < num:
                cost += (num - ans + k - 1) // k
                ans = ((num - ans + k - 1) // k) * k - (num - ans)
            else:
                ans -= num

        mod = 10**9 + 7

        return ((cost * (cost + 1)) // 2) % mod
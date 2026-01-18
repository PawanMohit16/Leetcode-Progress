class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay)
        n = len(bloomDay)

        if n < m * k:
            return -1

        while low <= high:
            mid = (low + high) // 2
            temp_m = m

            for i in range(n-k+1):
                if flower <= mid:
                    if temp_m 
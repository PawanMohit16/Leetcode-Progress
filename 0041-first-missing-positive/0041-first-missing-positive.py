class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1

        for num in sorted(nums):
            if num < 1 or num < n:
                continue
            
            elif num == n:
                n += 1

            else:
                return n

        return n
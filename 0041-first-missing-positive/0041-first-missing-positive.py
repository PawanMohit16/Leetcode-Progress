class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = max(nums)
        myset = set(nums)

        if n < 0:
            return 1

        for i in range(1,n):
            if i not in myset:
                return i


        return n + 1
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = (10 ** 9) + 7
        for i in range(len(queries)):
            l, r, k, v = queries[i]

            while l <= r:
                nums[l] = (nums[l] * v) % mod
                l += k

        res = nums[0]

        for i in range(1,len(nums)):
            res ^= nums[i]

        return res
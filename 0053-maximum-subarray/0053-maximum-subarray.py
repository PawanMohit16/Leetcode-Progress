class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxie = nums[0]

        for num in nums:
            curr += num
            maxie = max(maxie, curr)

            if curr < 0:
                curr = 0

        return maxie
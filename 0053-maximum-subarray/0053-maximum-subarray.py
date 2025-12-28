class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxie = nums[0]

        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxie = max(maxie, cursum)

        return maxie
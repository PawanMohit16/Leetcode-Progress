class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxie = nums[0]
        curr = nums[0]
        n = len(nums)

        for i in range(1, n):
            if curr < 0 and nums[i] > curr:
                curr = nums[i]
            else:
                curr += nums[i]

            maxie = max(maxie, curr)    

        return maxie 
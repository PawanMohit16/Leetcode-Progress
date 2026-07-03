class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = 0

        for i in range(len(nums)):
            maxie = nums[i]
            minie = nums[i]
            for j in range(i, len(nums)):
                maxie = max(maxie, nums[j])
                minie = min(minie, nums[j])
                ans += maxie - minie

        return ans


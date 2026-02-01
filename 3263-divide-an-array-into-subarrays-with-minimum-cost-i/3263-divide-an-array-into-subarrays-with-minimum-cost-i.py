class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sum = nums[0]
        minie1 = 51
        minie2 = 51
        for i in range(1,len(nums)):
            if nums[i] < minie1:
                minie2 = minie1
                minie1 = nums[i]
                continue
            elif nums[i] < minie2:
                minie2 = nums[i]

        return sum + minie1 + minie2



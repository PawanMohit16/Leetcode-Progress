class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minie = nums[0]

        while low <= high:
            mid = (high + low) // 2
            minie = min(minie, nums[mid])

            if nums[low] <= nums[mid]:
                minie = min(minie, nums[low])
                low = mid + 1

            else:
                high = mid - 1


        return minie
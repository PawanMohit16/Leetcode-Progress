class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        n = high + 1

        while low <= high:
            mid = (low + high) // 2

            if 0 < mid < n - 1 and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            elif mid < n - 1 and nums[mid + 1] > nums[mid]:
                low = mid + 1  

            elif mid > 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1

            else:
                return low
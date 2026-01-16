class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        n = high + 1

        if n == 1 or nums[0] > nums[1]:
            return 0

        if nums[n-1] > nums[n-2]:
            return high

        while low <= high:
            mid = (low + high) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid + 1] > nums[mid]:
                low = mid + 1  

            else:
                high = mid - 1

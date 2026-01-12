class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = len(nums), -1
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1

            elif nums[mid] == target:
                start = min(start, mid)
                high = mid - 1

            else:
                low = mid + 1

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] == target:
                end = max(end, mid)
                low = mid + 1
            
            else:
                high = mid - 1


        
        if start == -1 or end == -1:
            return [-1, -1]

        else:
            return [start, end]
        
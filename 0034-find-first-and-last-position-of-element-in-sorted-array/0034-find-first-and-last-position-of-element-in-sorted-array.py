class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = len(nums)-1, -1
        low, high = 0, len(nums)-1
        
        def bs(low, high):

            if low <= high:
                nonlocal start, end
                mid = (low + high) // 2

                if nums[mid] > target:
                    bs(low, mid - 1)

                elif nums[mid] == target:
                    start = min(mid, start)
                    end = max(mid, end)
                    bs(mid + 1, high)
                    bs(low, mid - 1)
                else:
                    bs(mid + 1, high)



        
        bs(low, high)
        if end == -1:
            return [-1, -1]
        
        return [start, end]

        
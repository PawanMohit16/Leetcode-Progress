class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        window = []
        mysum = 0

        while left <= right and right < len(nums):
            mysum += nums[right]
            while mysum >= target:
                window.append(right - left +  1) 
                mysum -= nums[left]
                left += 1
        
            right += 1

        if window:
            return min(window)
        else:
            return 0


        
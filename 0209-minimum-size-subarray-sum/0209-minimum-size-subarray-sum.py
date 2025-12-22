class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        result = 10 ** 5 + 1
        mysum = 0

        for right in range(len(nums)):
            mysum += nums[right]
            while mysum >= target:
                result = min(result, right - left +  1) 
                mysum -= nums[left]
                left += 1
        
            right += 1

        if result == 10 ** 5 + 1:
            return 0
        else:
            return result


        
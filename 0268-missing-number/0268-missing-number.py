class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = (n * (n + 1)) // 2
        mysum = 0

        for num in nums:
            mysum += num
        
        return summ - mysum
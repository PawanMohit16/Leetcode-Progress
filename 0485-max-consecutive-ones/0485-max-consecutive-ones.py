class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxie = 0
        for num in nums:
            if num != 1:
                counter = 0
            else:
                counter += 1
                maxie = max(maxie, counter)
            
        return maxie
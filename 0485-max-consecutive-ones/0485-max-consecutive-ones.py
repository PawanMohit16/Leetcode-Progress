class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxie = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
                maxie = max(maxie, curr)
            else:
                curr = 0
        return maxie

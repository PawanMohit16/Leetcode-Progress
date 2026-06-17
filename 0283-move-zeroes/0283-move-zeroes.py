class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        n = len(nums)
        for r in range(n):
            
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]

            if nums[l] != 0:
                l += 1
            
        
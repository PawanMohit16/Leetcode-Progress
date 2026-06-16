class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        
        for i in range(1,n):
            if nums[l] != nums[i]:
                l += 1
                nums[l] = nums[i]
            else:
                continue

        return l+1

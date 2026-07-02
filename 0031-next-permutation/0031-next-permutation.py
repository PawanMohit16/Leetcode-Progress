class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n - 2

        for i in range(n-1,0,-1):
            if nums[idx] < nums[i]:
                break

            idx -= 1
        
        if idx == -1:
            for i in range(n // 2):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]

        elif idx == n - 2:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

        else:
            for i in range(n-1, idx, -1):
                if nums[i] > nums[idx]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    break
            
            for i in range(idx+1,(n+idx+1)//2):
                nums[i], nums[n+idx-i] = nums[n+idx-i], nums[i]


            


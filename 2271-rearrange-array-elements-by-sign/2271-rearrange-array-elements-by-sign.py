class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        for num in range(len(nums)):
            if nums[num] > 0:
                even.append(nums[num])

            else:
                odd.append(nums[num])

        ans = []
                
        for i in range(len(even)):
            ans.append(even.pop(0))
            ans.append(odd.pop(0))

        return ans
        
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ecnt = 0
        ocnt = 1
        n = len(nums)
        ans = [None] * n

        for num in nums:
            if num > 0:
                ans[ecnt] = num
                ecnt += 2
            else:
                ans[ocnt] = num
                ocnt += 2

        return ans
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        votes = 1

        for i in range(1, n) :
            if nums[i] == candidate:
                votes += 1

            else:
                if votes == 0:
                    candidate = nums[i]
                    votes = 1
                votes -= 1

        return candidate


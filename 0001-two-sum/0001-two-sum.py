class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for _, num in enumerate(nums):
            if target - num  in hashmap:
                return [_, hashmap[target - num]]

            else:
                hashmap[num] = _
        
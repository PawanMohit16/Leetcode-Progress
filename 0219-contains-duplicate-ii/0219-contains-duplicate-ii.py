class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}

        for idx, num in enumerate(nums):
            if num not in dict:
                dict[num] = idx
            else:
                if abs(dict[num] - idx) <= k:
                    return True
                dict[num] = idx

        return False 
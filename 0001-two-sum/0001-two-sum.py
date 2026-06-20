class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(num)):

            if target - num[i] in hashmap:
                return [i, hashmap[target-num[i]]]
            if num[i] not in hashmap:
                hashmap[num[i]] = i
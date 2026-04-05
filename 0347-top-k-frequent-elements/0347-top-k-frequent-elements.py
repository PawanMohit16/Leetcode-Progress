class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myset = {}

        for num in nums:
            if num not in myset:
                myset[num] = 1
            else:
                myset[num] += 1

        sorted_keys = [key for key, value in sorted(myset.items(), key=lambda item: item[1], reverse=True)]        
        
        return sorted_keys[:k]


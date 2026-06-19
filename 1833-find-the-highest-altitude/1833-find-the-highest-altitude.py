class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxie = 0
        curr = 0
        for num in gain:
            curr += num
            maxie = max(curr, maxie)

        return maxie
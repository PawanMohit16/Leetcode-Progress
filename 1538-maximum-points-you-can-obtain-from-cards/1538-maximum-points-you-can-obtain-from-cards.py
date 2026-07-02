class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = 0
    
        n = len(cardPoints)
        l = k-1
        r = n-1
        rsum = 0
        for i in range(k):
            curr += cardPoints[i]

        maxie = curr

        for i in range(r, r-k, -1):
            rsum += cardPoints[i]
            curr -= cardPoints[l]
            l -= 1
            maxie = max(maxie, rsum + curr)

        return maxie

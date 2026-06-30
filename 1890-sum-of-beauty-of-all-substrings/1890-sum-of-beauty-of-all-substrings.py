class Solution:
    def beautySum(self, s: str) -> int:
        alphabets = {}
        ans = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in alphabets:
                    alphabets[s[j]] = 1
                else:
                    alphabets[s[j]] += 1

                arr = list(alphabets.values())
                ans += max(arr) - min(arr)
            alphabets = {}
        return ans
            

        


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        mydict = {}
        maxie = 0
    
        for right in range(len(s)):
            if s[right] not in mydict:
                mydict[s[right]] = 1
            else:
                mydict[s[right]] += 1

            maxie = max(maxie, mydict[s[right]])

            while (right - left + 1) - maxie > k:
                mydict[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
                
        
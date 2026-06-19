class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = 0
        myset = {}

        for c in s:
            if c not in myset:
                myset[c] = 1
            else:
                myset[c] += 1

        for i in range(len(s)):
            if myset[s[i]] == 1:
                return i

        return -1

            
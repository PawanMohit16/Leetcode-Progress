class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict = {}
        
        for s in s1:
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] += 1
        
        acopy = dict.copy()
        
        left = 0
        for right in range(len(s2)):
            if s2[right] in dict:
                dict[s2[right]] -= 1

            # keep window size == len(s1)
            if right - left + 1 > len(s1):
                if s2[left] in dict:
                    dict[s2[left]] += 1
                left += 1

            if set(dict.values()) == {0}:
                return True

        return False

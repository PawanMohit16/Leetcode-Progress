class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1, even2 = {}, {}
        odd1, odd2 = {}, {}

        for i in range(len(s1)):
            if i % 2 == 0:
                if s1[i] in even1:
                    even1[s1[i]] += 1
                else:
                    even1[s1[i]] = 1

                if s2[i] in even2:
                    even2[s2[i]] += 1
                else:
                    even2[s2[i]] = 1

            else:
                if s1[i] in odd1:
                    odd1[s1[i]] += 1
                else:
                    odd1[s1[i]] = 1

                if s2[i] in odd2:
                    odd2[s2[i]] += 1
                else:
                    odd2[s2[i]] = 1

        return even1 == even2 and odd1 == odd2
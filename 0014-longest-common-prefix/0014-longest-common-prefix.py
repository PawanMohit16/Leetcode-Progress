class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for j in strs[1:]:
                if i >= len(j) or j[i] != ch:
                    return strs[0][:i]

        return strs[0]

class Solution:
    def maxDepth(self, s: str) -> int:
        maxie = 0
        count = 0

        for letter in s:
            if letter == '(':
                count += 1
                maxie = max(maxie, count)
            
            elif letter == ')':
                count -= 1

        return maxie
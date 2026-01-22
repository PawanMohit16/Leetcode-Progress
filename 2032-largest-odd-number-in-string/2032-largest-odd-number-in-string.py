class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxie = -1
        for i in range(len(num)):
            mynum = int(num[i])
            if mynum % 2 == 1:
                maxie = i
        if maxie == -1:
            return ''
        return num[:maxie+1]
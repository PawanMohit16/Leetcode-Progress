class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(' ')
        ans = ''
        print(arr)
        for word in arr[::-1]:
            if not word == '':
                ans += word + ' '

        return ans[:-1]


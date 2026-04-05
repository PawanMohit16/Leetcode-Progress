class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        if rows == 1:
            return encodedText

        res = ''
        n = len(encodedText)
        c = n // rows

        for i in range(c):
            for j in range(i, n, c+1):
                res += encodedText[j]

        print(res)

        return res.rstrip()

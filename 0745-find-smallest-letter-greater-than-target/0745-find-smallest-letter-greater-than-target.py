class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)
        minie = 3000

        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (low + high) // 2
            temp = ord(letters[mid])
            if temp == target + 1:
                return letters[mid]

            elif temp > target:
                minie = min(minie, temp)
                high = mid - 1
            
            else:
                low = mid + 1

        if minie == 3000:
            return letters[0]
        else:
            return chr(minie)


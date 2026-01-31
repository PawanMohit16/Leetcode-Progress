class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    
        n = len(letters)
        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid

            else:
                low = mid + 1

        if low >= n:
            return letters[0]
        else:
            return letters[low]


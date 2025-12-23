class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if x <= arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:k+2]

        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left:right + 1]

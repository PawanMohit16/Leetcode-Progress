class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:

        occupiedIntervals.sort()
        processed = []

        for start, end in occupiedIntervals:
            if end < freeStart or start > freeEnd:
                processed.append([start, end])
            elif start >= freeStart and end <= freeEnd:
                continue
            elif start < freeStart and end <= freeEnd:
                processed.append([start, freeStart - 1])
            elif start >= freeStart and end > freeEnd:
                processed.append([freeEnd + 1, end])
            else:
                processed.append([start, freeStart - 1])
                processed.append([freeEnd + 1, end])

        processed.sort()

        res_arr = [[-2, -2]]

        for start, end in processed:
            pstart, pend = res_arr[-1]

            if start <= pend + 1:
                res_arr[-1][1] = max(pend, end)
            else:
                res_arr.append([start, end])

        return res_arr[1:]
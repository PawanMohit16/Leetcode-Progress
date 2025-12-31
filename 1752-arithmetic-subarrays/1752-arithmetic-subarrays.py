class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        m = len(l)
        res = []

        for i in range(m):
            ref = sorted(nums[l[i]:r[i] + 1])
            d = ref[1] - ref[0]

            if d == 0:
                res.append(len(set(ref)) == 1)
                continue

            res.append(ref == list(range(ref[0], ref[-1] + 1, d)))

        return res

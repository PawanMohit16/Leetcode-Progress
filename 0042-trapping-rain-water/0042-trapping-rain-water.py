class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        l = 0
        r = 0
        llist = []
        rlist = [0] * n

        for h in height:
            l = max(l, h)
            llist.append(l)

        for i in range(n - 1, -1, -1):
            r = max(r, height[i])
            rlist[i] = r

        water = 0
        for i in range(n):
            water += min(llist[i], rlist[i]) - height[i]

        return water

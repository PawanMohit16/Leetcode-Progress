class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        qset = set(map(tuple, queens))
        res = []
        kr, kc = king

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            r, c = kr + dr, kc + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if (r, c) in qset:
                    res.append([r, c])
                    break
                r += dr
                c += dc

        return res

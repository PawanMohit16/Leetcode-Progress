class Solution:
    def judgeCircle(self, moves: str) -> bool:
        rc, dc = 0, 0

        for move in moves:
            if move == 'R':
                rc += 1
            elif move == 'L':
                rc -= 1

            elif move == 'D':
                dc += 1

            else:
                dc -= 1

        return dc == rc == 0
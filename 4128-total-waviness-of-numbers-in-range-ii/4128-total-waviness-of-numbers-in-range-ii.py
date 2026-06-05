from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, p1, p2, started, tight):
                if pos == len(s):
                    return (1, 0)  # (count, total_waviness)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started:
                        if d == 0:
                            cnt, wav = dfs(
                                pos + 1, 10, 10, False, ntight
                            )
                        else:
                            cnt, wav = dfs(
                                pos + 1, d, 10, True, ntight
                            )

                        total_cnt += cnt
                        total_wav += wav
                        continue

                    add = 0
                    if p2 != 10:
                        if (p1 > p2 and p1 > d) or \
                           (p1 < p2 and p1 < d):
                            add = 1

                    cnt, wav = dfs(
                        pos + 1,
                        d,      # new last digit
                        p1,     # new second last digit
                        True,
                        ntight
                    )

                    total_cnt += cnt
                    total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            return dfs(0, 10, 10, False, True)[1]

        return solve(num2) - solve(num1 - 1)
class SolutionRecursive:
    def CountWays(self, p: int, q: int, r: int) -> int:
        def rec(
            p: int,
            q: int,
            r: int,
            prev: int | None = None,
        ) -> int:
            if p < 0 or q < 0 or r < 0:
                return 0
            if p == 0 and q == 0 and r == 0:
                return 1

            if prev is None:
                return rec(p - 1, q, r, 0) + rec(p, q - 1, r, 1) + rec(p, q, r - 1, 2)
            elif prev == 0:
                return rec(p, q - 1, r, 1) + rec(p, q, r - 1, 2)
            elif prev == 1:
                return rec(p - 1, q, r, 0) + rec(p, q, r - 1, 2)
            else:
                return rec(p - 1, q, r, 0) + rec(p, q - 1, r, 1)

        return rec(p, q, r)


class SolutionRecursiveRefactor:
    def CountWays(self, p: int, q: int, r: int) -> int:
        def rec(
            p: int,
            q: int,
            r: int,
            prev: int | None = None,
        ) -> int:
            if p == 0 and q == 0 and r == 0:
                return 1

            res = 0
            if prev != 0 and p > 0:
                res += rec(p - 1, q, r, 0)
            if prev != 1 and q > 0:
                res += rec(p, q - 1, r, 1)
            if prev != 2 and r > 0:
                res += rec(p, q, r - 1, 2)
            return res

        return rec(p, q, r)


class SolutionTopDown:
    def CountWays(self, p: int, q: int, r: int) -> int:
        def rec(
            p: int,
            q: int,
            r: int,
            prev: int | None = None,
        ) -> int:
            if p == 0 and q == 0 and r == 0:
                return 1

            key = (p, q, r, prev)
            if key not in mem:
                res = 0
                if prev != 0 and p > 0:
                    res += rec(p - 1, q, r, 0)
                if prev != 1 and q > 0:
                    res += rec(p, q - 1, r, 1)
                if prev != 2 and r > 0:
                    res += rec(p, q, r - 1, 2)
                mem[key] = res
            return mem[key]

        mem = dict()
        return rec(p, q, r)


class SolutionBottomUp:
    def CountWays(self, p: int, q: int, r: int) -> int:
        dp = [
            [[[0 for _ in range(4)] for _ in range(r + 1)] for _ in range(q + 1)]
            for _ in range(p + 1)
        ]
        dp[0][0][0][3] = 1

        for pi in range(p + 1):
            for qi in range(q + 1):
                for ri in range(r + 1):
                    for prev in range(4):
                        val = dp[pi][qi][ri][prev]
                        if val == 0:
                            continue
                        if pi < p and prev != 0:
                            dp[pi + 1][qi][ri][0] += val
                        if qi < q and prev != 1:
                            dp[pi][qi + 1][ri][1] += val
                        if ri < r and prev != 2:
                            dp[pi][qi][ri + 1][2] += val

        return sum(dp[p][q][r][prev] for prev in range(3))


if __name__ == "__main__":
    p = 2
    q = 2
    r = 2
    print(SolutionRecursive().CountWays(p, q, r))
    print(SolutionRecursiveRefactor().CountWays(p, q, r))
    print(SolutionTopDown().CountWays(p, q, r))
    print(SolutionBottomUp().CountWays(p, q, r))

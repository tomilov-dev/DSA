class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        def backtrack(i: int) -> bool:
            if i >= len(m):
                return all(size == t for size in square)

            for side in range(len(square)):
                if square[side] + m[i] <= t:
                    square[side] += m[i]
                    if backtrack(i + 1):
                        return True
                    square[side] -= m[i]
                if square[side] == 0:
                    break
            return False

        m = matchsticks
        msum = sum(m)
        if msum <= 0 or msum % 4 != 0:
            return False

        t = msum // 4
        if max(m) > t:
            return False

        m.sort(reverse=True)
        square = [0, 0, 0, 0]
        return backtrack(0)


class SolutionDPBottomUp:
    def makesquare(
        self,
        matchsticks: list[int],
    ) -> bool:
        m = matchsticks
        n = len(m)
        total = sum(m)
        if total % 4 != 0:
            return False

        t = total // 4
        if max(m) > t:
            return False

        full_mask = (1 << n) - 1
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                new_mask = mask | (1 << i)
                if dp[mask] + m[i] <= t:
                    dp[new_mask] = (dp[mask] + m[i]) % t

        return dp[full_mask] == 0


if __name__ == "__main__":
    matchsticks = [1, 1, 2, 2, 2]
    matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1]
    print(Solution().makesquare(matchsticks))

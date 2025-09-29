class SolutionRecursive:
    def stoneGame(self, piles: list[int]) -> bool:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0

            alice_turn = (i + j) % 2
            take = max(piles[i], piles[j])
            take = take if alice_turn else -take
            return take + max(
                rec(i + 1, j),
                rec(i, j - 1),
            )

        n = len(piles)
        res = rec(0, n - 1)
        return res >= 0


class SolutionTopDown:
    def stoneGame(self, piles: list[int]) -> bool:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0

            key = (i, j)
            if key not in mem:
                alice_turn = (i + j) % 2
                take = max(piles[i], piles[j])
                take = take if alice_turn else -take
                mem[key] = take + max(
                    rec(i + 1, j),
                    rec(i, j - 1),
                )
            return mem[key]

        n = len(piles)
        mem = {}
        res = rec(0, n - 1)
        return res >= 0


class SolutionBottomUp:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],
                    piles[j] - dp[i][j - 1],
                )
        return dp[0][n - 1] > 0


class SolutionGreedy:
    def stoneGame(self, piles: list[int]) -> bool:
        # первый игрок не может проиграть если будет играть оптимально
        return True


if __name__ == "__main__":
    piles = [5, 3, 4, 5]
    sol = SolutionBottomUp()
    print(sol.stoneGame(piles))

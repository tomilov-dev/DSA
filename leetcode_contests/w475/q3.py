MIN = -(10**10)


class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        def rec(i: int, j: int, totalCost: int) -> int:
            if i >= m or j >= n:
                return MIN

            key = (i, j, totalCost)
            if key not in mem:
                score = grid[i][j]
                cost = costsMap[score]
                totalCost += cost
                if totalCost > k:
                    return MIN

                if i == m - 1 and j == n - 1:
                    return score

                bottom = rec(i + 1, j, totalCost)
                right = rec(i, j + 1, totalCost)
                best = max(bottom, right)
                mem[key] = score + best if best != MIN else MIN
            return mem[key]

        costsMap = {0: 0, 1: 1, 2: 1}
        m = len(grid)
        n = len(grid[0])
        mem = {}
        res = rec(0, 0, 0)
        return -1 if res == MIN else res


if __name__ == "__main__":

    grid = [[0, 1], [2, 0]]
    k = 1

    # grid = [[0, 1], [1, 2]]
    # k = 1

    sol = Solution()
    print(sol.maxPathScore(grid, k))

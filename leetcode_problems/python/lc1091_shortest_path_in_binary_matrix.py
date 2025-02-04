from collections import deque


class Solution:
    def shortestPathBinaryMatrix(
        self,
        grid: list[list[int]],
    ) -> int:
        def inbound(
            i: int,
            j: int,
        ) -> bool:
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def is_finish(i: int, j: int) -> bool:
            return i == len(grid) - 1 and j == len(grid[0]) - 1

        if grid[0][0] == 1:
            return -1

        visited = [[False] * len(grid[i]) for i in range(len(grid))]
        q = deque([(0, 0, 1)])
        visited[0][0] = True

        while q:
            i, j, c = q.popleft()
            if is_finish(i, j):
                return c

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y
                    if not inbound(ni, nj):
                        continue
                    if grid[ni][nj] == 1:
                        continue
                    if visited[ni][nj]:
                        continue
                    q.append((ni, nj, c + 1))
                    visited[ni][nj] = True

        return -1


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]
    print(Solution().shortestPathBinaryMatrix(grid))

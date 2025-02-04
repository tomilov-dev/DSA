class Solution:
    def solve(
        self,
        board: list[list[str]],
    ) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def inbound(
            i: int,
            j: int,
        ) -> bool:
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        def dfs(i: int, j: int):
            if not inbound(i, j):
                return None
            if board[i][j] == "X":
                return None
            if visited[i][j]:
                return None

            visited[i][j] = True
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        visited = [[False] * len(board[i]) for i in range(len(board))]
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)

        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print(Solution().solve(board))

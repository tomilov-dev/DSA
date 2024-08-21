class Solution:
    def countBattleships(
        self,
        board: list[list[str]],
    ) -> int:
        if not board:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    if (i == 0 or board[i - 1][j] == ".") and (
                        j == 0 or board[i][j - 1] == "."
                    ):
                        count += 1

        return count


if __name__ == "__main__":
    board = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]

    # board = [
    #     ["X", "X", "X"],
    # ]

    print(Solution().countBattleships(board))

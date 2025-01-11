class Solution:
    def validate_rows(
        self,
        b: list[list[str]],
    ) -> bool:
        for i in range(len(b)):
            mem = set([])
            for j in range(len(b[0])):
                if b[i][j] == ".":
                    continue
                if b[i][j] in mem:
                    return False
                mem.add(b[i][j])
        return True

    def validate_cols(
        self,
        b: list[list[str]],
    ) -> bool:
        for j in range(len(b[0])):
            mem = set()
            for i in range(len(b)):
                if b[i][j] == ".":
                    continue
                if b[i][j] in mem:
                    return False
                mem.add(b[i][j])
        return True

    def validate_grids(
        self,
        b: list[list[str]],
    ) -> bool:
        def index(i, j) -> int:
            return (i // 3) * 3 + (j // 3)

        maps = [set() for _ in range(9)]
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] == ".":
                    continue
                mi = index(i, j)
                if b[i][j] in maps[mi]:
                    return False
                maps[mi].add(b[i][j])
        return True

    def isValidSudoku(
        self,
        board: list[list[str]],
    ) -> bool:
        return (
            self.validate_rows(board)
            and self.validate_cols(board)
            and self.validate_grids(board)
        )


class Solution2:
    def isValidSudoku(
        self,
        board: list[list[str]],
    ) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                grid_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in grids[grid_index]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grids[grid_index].add(board[i][j])

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    print(Solution2().isValidSudoku(board))

class Solution:
    def exist(
        self,
        board: list[list[str]],
        word: str,
    ) -> bool:
        def backtrack(i: int, j: int, wp: int) -> bool:
            if wp >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if word[wp] != board[i][j]:
                return False
            if used[i][j]:
                return False

            used[i][j] = True
            steps = [
                (0, -1),
                (-1, 0),
                (0, +1),
                (+1, 0),
            ]
            for y, z in steps:
                if backtrack(i + y, j + z, wp + 1):
                    return True

            used[i][j] = False
            return False

        used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False


class SolutionInplace:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i: int, j: int, wp: int) -> bool:
            if wp == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if word[wp] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            steps = [
                (0, -1),
                (-1, 0),
                (0, +1),
                (+1, 0),
            ]
            for y, z in steps:
                if backtrack(i + y, j + z, wp + 1):
                    return True

            board[i][j] = temp
            return False

        if len(word) > len(board) * len(board[0]):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCCED"

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "SEE"

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCB"

    board = [
        ["a", "b"],
        ["c", "d"],
    ]
    word = "abcd"
    print(Solution().exist(board, word))

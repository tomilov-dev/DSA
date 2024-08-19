class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0

        index = 0
        while index < len(s):
            if s[index] == "X":
                index += 3
                moves += 1
            else:
                index += 1

        return moves


if __name__ == "__main__":
    s = "XXOX"
    print(Solution().minimumMoves(s))

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mp = {"L": -1, "R": 1}
        return abs(sum(mp.get(m, 0) for m in moves)) + sum(m == "_" for m in moves)


if __name__ == "__main__":
    moves = "L_RL__R"
    moves = "_R__LL_"
    moves = "_______"
    print(Solution().furthestDistanceFromOrigin(moves))

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


if __name__ == "__main__":
    matchsticks = [1, 1, 2, 2, 2]
    matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1]
    print(Solution().makesquare(matchsticks))

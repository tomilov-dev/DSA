class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        vals = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        n = len(s)

        xpref = [0] * (n + 1)
        ypref = [0] * (n + 1)
        for i, c in enumerate(s):
            xpref[i + 1] = xpref[i] + vals[c][0]
            ypref[i + 1] = ypref[i] + vals[c][1]

        uniq: set[tuple[int, int]] = set()
        for i in range(n - k + 1):
            x = xpref[i] + (xpref[n] - xpref[i + k])
            y = ypref[i] + (ypref[n] - ypref[i + k])
            uniq.add((x, y))
        return len(uniq)


if __name__ == "__main__":
    s = "LUL"
    k = 1

    s = "UDLR"
    k = 4

    s = "UU"
    k = 1
    print(Solution().distinctPoints(s, k))

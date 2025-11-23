import bisect


class SolutionTLE:
    def digits(self, s: str) -> list[int]:
        digits = []
        for snum in s:
            digits.append(int(snum))
        return digits

    def sumAndMultiply(
        self,
        s: str,
        queries: list[list[int]],
    ) -> list[int]:
        MOD = 10**9 + 7

        digits = self.digits(s)
        n = len(digits)

        psum = [0] * (n + 1)
        pdigit = [0] * (n + 1)
        pcount = [0] * (n + 1)
        for i in range(len(digits)):
            d = digits[i]
            psum[i + 1] = d + psum[i]
            if d == 0:
                pdigit[i + 1] = pdigit[i]
                pcount[i + 1] = pcount[i]
            else:
                pdigit[i + 1] = pdigit[i] * 10 + d
                pcount[i + 1] = pcount[i] + 1

        res = []
        cache: dict[tuple[int, int], int] = dict()
        for i, j in queries:
            key = (i, j)
            if key in cache:
                res.append(cache[key])
                continue

            xsum = psum[j + 1] - psum[i]
            xci = pcount[i]
            xcj = pcount[j + 1]
            xdig = pdigit[j + 1] % (10 ** (xcj - xci))
            xres = (xsum * xdig) % MOD
            cache[key] = xres
            res.append(xres)
        return res


class SolutionTLE2:
    def digits(self, s: str) -> list[int]:
        digits = []
        for snum in s:
            digits.append(int(snum))
        return digits

    def sumAndMultiply(
        self,
        s: str,
        queries: list[list[int]],
    ) -> list[int]:
        MOD = 10**9 + 7
        digits = self.digits(s)

        nz_index = []
        for i, digit in enumerate(digits):
            if digit == 0:
                continue
            nz_index.append(i)

        psum = [0]
        for i in nz_index:
            psum.append(digits[i] + psum[-1])

        res = []
        cache: dict[tuple[int, int], int] = dict()
        for i, j in queries:
            key = (i, j)
            if key in cache:
                res.append(cache[key])
                continue

            l = bisect.bisect_left(nz_index, i)
            r = bisect.bisect_right(nz_index, j)
            if l == r:
                res.append(0)
                continue

            xdig = 0
            for nzi in nz_index[l:r]:
                xdig = (10 * xdig + digits[nzi]) % MOD
            xsum = psum[r] - psum[l]
            xres = (xdig * xsum) % MOD
            cache[key] = xres
            res.append(xres)
        return res


class Solution:
    def digits(self, s: str) -> list[int]:
        digits = []
        for snum in s:
            digits.append(int(snum))
        return digits

    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        digits = self.digits(s)

        n = len(digits)
        dmat = [[0] * n for _ in range(n)]
        for i in range(n):
            xdig = 0
            for j in range(i, n):
                if digits[j] != 0:
                    xdig = xdig * 10 + digits[j]
                dmat[i][j] = xdig

        psum = [0] * (n + 1)
        for i in range(len(digits)):
            d = digits[i]
            psum[i + 1] = d + psum[i]

        res = []
        for l, r in queries:
            xdig = dmat[l][r]
            xsum = psum[r + 1] - psum[l]
            res.append((xdig * xsum) % MOD)
        return res


if __name__ == "__main__":
    s = "10203004"
    queries = [[0, 7], [1, 3], [4, 6]]

    # s = "1000"
    # queries = [[0, 3], [1, 1]]

    # s = "9876543210"
    # queries = [[0, 9]]

    print(Solution().sumAndMultiply(s, queries))

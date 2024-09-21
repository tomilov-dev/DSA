class Solution:
    def bs1(self, row: list[int]) -> int:
        lo = 0
        hi = len(row) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if row[mid] > 0:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

    def kWeakestRows(
        self,
        mat: list[list[int]],
        k: int,
    ) -> list[int]:
        strength = [(i, self.bs1(row) + 1) for i, row in enumerate(mat)]
        strength.sort(key=lambda x: (x[1], x[0]))
        return [x[0] for x in strength[:k]]


if __name__ == "__main__":
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3
    print(Solution().kWeakestRows(mat, k))

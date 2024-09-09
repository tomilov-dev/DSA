class Solution:
    def count(self, code: list[int], k: int) -> list[int]:
        sums = []
        for i in range(len(code)):
            cursum = 0
            if k > 0:
                for j in range(1, k + 1):
                    cursum += code[(i + j) % len(code)]
            elif k < 0:
                for j in range(1, abs(k) + 1):
                    cursum += code[(i - j) % len(code)]
            sums.append(cursum)
        return sums

    def decrypt(
        self,
        code: list[int],
        k: int,
    ) -> list[int]:
        if k == 0:
            return [0 for _ in range(len(code))]
        elif k > 0:
            return self.count(code, k)
        else:
            return self.count(code, k)


if __name__ == "__main__":
    code = [5, 7, 1, 4]
    k = 3
    print(Solution().decrypt(code, k))

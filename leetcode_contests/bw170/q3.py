class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        v = list(range(n, 0, -1))
        sm = sum(v)
        i = 0

        while i < n:
            if sm == target:
                break

            if sm - 2 * v[i] >= target:
                sm -= 2 * v[i]
                v[i] *= -1
                i += 1
            else:
                i += 1

        if sm != target:
            return []
        return list(sorted(v))


if __name__ == "__main__":
    n = 3
    target = 0

    # n = 1
    # target = 10000000000
    print(Solution().lexSmallestNegatedPerm(n, target))

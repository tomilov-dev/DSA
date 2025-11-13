class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        mem = {}
        for idx, num in enumerate(nums):
            if num not in mem:
                mem[num] = []
            mem[num].append(idx)

        mini = 10**9
        for idxs in mem.values():
            n = len(idxs)
            if n < 3:
                continue
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        dist = (
                            abs(idxs[i] - idxs[j])
                            + abs(idxs[j] - idxs[k])
                            + abs(idxs[k] - idxs[i])
                        )
                        mini = min(mini, dist)
        return mini if mini != 10**9 else -1


if __name__ == "__main__":

    sol = Solution()
    res = sol.minimumDistance([1, 2, 1, 1, 3])
    res = sol.minimumDistance([1, 1, 2, 3, 2, 1, 2])
    print(res)

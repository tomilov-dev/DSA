class Solution:
    def combinationSum2(
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        def backtrack(i: int, cursum: int) -> None:
            if cursum == target:
                res.append(stack[:])
                return
            elif cursum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > target - cursum:
                    break

                stack.append(candidates[j])
                cursum += candidates[j]
                backtrack(j + 1, cursum)
                stack.pop()
                cursum -= candidates[j]

        candidates.sort()
        res = []
        stack = []
        backtrack(0, 0)
        return list(map(list, res))


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    # candidates = [2, 5, 2, 1, 2]
    # target = 5
    print(Solution().combinationSum2(candidates, target))

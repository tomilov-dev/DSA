class Solution:
    def combinationSum(
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        def backtrack(i: int, cursum: int) -> None:
            if cursum == target:
                res.append(stack[:])
                return None
            elif cursum > target:
                return None

            for j in range(i, len(candidates)):
                stack.append(candidates[j])
                cursum += candidates[j]
                backtrack(j, cursum)
                stack.pop()
                cursum -= candidates[j]

        res = []
        stack = []
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))

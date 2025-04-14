class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        def large(seqA: list[int], seqB: list[int]) -> bool:
            if len(seqA) > len(seqB):
                return True
            elif len(seqA) < len(seqB):
                return False
            else:
                for i in range(len(seqA)):
                    if seqA[i] == seqB[i]:
                        continue
                    return seqA[i] > seqB[i]
                return False

        def backtrack(i: int) -> None:
            nonlocal stack
            nonlocal res
            nonlocal found

            if found:
                return

            if i >= len(stack):
                if large(stack, res):
                    res = stack[:]
                    found = True
                return None

            if stack[i] != -1:
                backtrack(i + 1)
                return None

            for num in range(n, 0, -1):
                if not nums[num]:
                    continue

                dist = 0 if num == 1 else num
                if i + dist >= len(stack) or stack[i + dist] != -1:
                    continue

                stack[i] = num
                stack[i + dist] = num
                nums[num] = False

                backtrack(i + 1)

                nums[num] = True
                stack[i] = -1
                stack[i + dist] = -1

        found = False
        nums = [True] * (n + 1)
        stack = [-1] * (1 + (n - 1) * 2)
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    n = 3
    print(Solution().constructDistancedSequence(n))

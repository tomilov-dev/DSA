class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack() -> bool:
            nonlocal count
            if len(stack) >= n:
                count += 1
                return count == k

            for char in "abc":
                if len(stack) > 0 and stack[-1] == char:
                    continue

                stack.append(char)
                if backtrack():
                    return True
                stack.pop()

            return False

        count = 0
        stack = []
        backtrack()
        return "".join(stack)


if __name__ == "__main__":
    n = 3
    k = 9
    print(Solution().getHappyString(n, k))

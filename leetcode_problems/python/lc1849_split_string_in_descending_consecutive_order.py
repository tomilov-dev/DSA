class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i: int, prev: str | None) -> bool:
            if i >= n and prev and len(prev) != n:
                return True

            for j in range(i, n):
                sub = s[i : j + 1]
                if prev is not None and not int(prev) - int(sub) == 1:
                    continue
                if backtrack(j + 1, sub):
                    return True
            return False

        n = len(s)
        return backtrack(0, None)


if __name__ == "__main__":
    s = "050043"
    s = "1234"
    s = "9080701"
    print(Solution().splitString(s))

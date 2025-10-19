class Solution:
    def lexw(self, s: str) -> int:
        weight = 0
        for c in s:
            weight = weight * 26 + (ord(c) - ord("a"))
        return weight

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def backtrack(n: int) -> None:
            nonlocal minw
            nonlocal minstr
            if n == 0:
                new = "".join(reversed(stack))
                cw = self.lexw(new)
                if cw > tw and cw < minw:
                    minw = cw
                    minstr = new
                return None

            for i, c in enumerate(count):
                if c == 0:
                    continue

                char = chr(ord("a") + i)

                stack.append(char)
                count[i] -= 1
                backtrack(n - 1)
                count[i] += 1
                stack.pop()

        if len(s) > len(target):
            return "".join(sorted(s))
        if len(s) < len(target):
            return ""

        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1

        tw = self.lexw(target)
        stack = []
        minstr = ""
        minw = float("inf")
        backtrack(len(target))
        return minstr


BASE = ""


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def geti(char: str) -> int:
            return ord(char) - ord("a")

        def getc(ind: int) -> str:
            return chr(ord("a") + ind)

        if len(s) > len(target):
            return "".join(sorted(s))
        if len(target) > len(s):
            return BASE

        l = 26
        count = [0] * l
        for char in s:
            count[geti(char)] += 1

        n = len(s)
        new = [""] * n
        for i, char in enumerate(target):
            ci = geti(char)
            if count[ci] > 0:
                new[i] = char
                count[ci] -= 1

        done = False

        print(count)
        print(new)

        return ""


if __name__ == "__main__":
    s = "abc"
    target = "bba"
    s = "leet"
    target = "code"
    # s = "baba"
    # target = "bbaa"
    sol = Solution()
    print(sol.lexGreaterPermutation(s, target))

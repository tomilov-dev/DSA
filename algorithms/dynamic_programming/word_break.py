class SolutionRecursive:
    def wordBreak(
        self,
        s: str,
        dictionary: list[str],
    ) -> bool:
        def rec(i: int) -> bool:
            if i >= n:
                return True

            for j in range(i, n):
                if s[i : j + 1] in words and rec(j + 1):
                    return True
            return False

        n = len(s)
        words = set(dictionary)
        return rec(0)


class SolutionTopDown:
    def wordBreak(
        self,
        s: str,
        dictionary: list[str],
    ) -> bool:
        def rec(i: int) -> bool:
            if i >= n:
                return True

            if i not in mem:
                mem[i] = False
                for word in words:
                    if s[i : i + len(word)] == word and rec(i + len(word)):
                        mem[i] = True
                        break

            return mem[i]

        n = len(s)
        mem = dict()
        words = set(dictionary)
        return rec(0)


class SolutionBottomUp:
    def wordBreak(
        self,
        s: str,
        dictionary: list[str],
    ) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in dictionary:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start : start + len(w)] == w:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    s = "ilike"
    dictionary = ["i", "like", "gfg"]

    s = "ilikegfg"
    dictionary = ["i", "like", "man", "india", "gfg"]

    # s = "ilikemangoes"
    # dictionary = ["i", "like", "man", "india", "gfg"]

    print(SolutionRecursive().wordBreak(s, dictionary))
    print(SolutionTopDown().wordBreak(s, dictionary))
    print(SolutionBottomUp().wordBreak(s, dictionary))

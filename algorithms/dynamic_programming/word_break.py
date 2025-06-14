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
                substr = s[i : j + 1]
                if substr in words and rec(j + 1):
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
                    substr = s[i : i + len(word)]
                    if substr == word and rec(i + len(word)):
                        mem[i] = True
                        return mem[i]
            return mem[i]

        n = len(s)
        words = set(dictionary)
        mem = {}
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

        # Здесь наблюдается запутанность с индексами
        # Потому что s и dp различаются по индексации на +1
        # Поэтому dp[start] - это ничто иное, как проверка подстроки s[: start] на "валидность"
        # Если s[: start] не является "валидной", то все дальнейшие проверки не имеют смысла
        # Если start = 0 - тогда 100% можно, потому что s[: start] пустая строка по определению
        for end in range(1, n + 1):
            for w in dictionary:
                start = end - len(w)
                if start >= 0 and dp[start] and w == s[start:end]:
                    dp[end] = True
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

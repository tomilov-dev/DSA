class SolutionRecursive:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def rec(i: int) -> bool:
            if i >= n:
                return True
            for j in range(i + 1, n + 1):
                if s[i:j] in word_map and rec(j):
                    return True
            return False

        n = len(s)
        word_map = set(wordDict)
        return rec(0)


class SolutionTopDown:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def rec(i: int) -> bool:
            if i >= n:
                return True
            key = i
            if key not in mem:
                mem[key] = False
                for j in range(i + 1, n + 1):
                    if s[i:j] in word_map and rec(j):
                        mem[key] = True
                        break
            return mem[key]

        n = len(s)
        mem = {}
        word_map = set(wordDict)
        return rec(0)


class SolutionBottomUp:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        word_map = set(wordDict)
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if s[i - 1 : j] in word_map and dp[i - 1]:
                    dp[j] = True
                    break
        return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = SolutionBottomUp()
    print(sol.wordBreak(s, wordDict))

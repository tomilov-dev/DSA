class Solution:
    def wordBreak(
        self,
        s: str,
        wordDict: list[str],
    ) -> bool:
        def backtrack(i: int) -> bool:
            nonlocal result
            if i >= n:
                print(cover)
                result = result or all(cover)
            if cover[i]:
                return backtrack(i + 1)

            for word in wordDict:
                end = i + len(word)
                if end >= n:
                    continue
                if s[i:end] != word:
                    continue

                for j in range(i, end):
                    cover[j] = True

                backtrack(i + 1)

                for j in range(i, end):
                    cover[j] = False

            return False

        result = False
        n = len(s)
        cover = [False] * n
        backtrack(0)
        return result


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

    print(Solution().wordBreak(s, wordDict))

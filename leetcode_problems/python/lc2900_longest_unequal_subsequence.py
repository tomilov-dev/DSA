class Solution:
    def getLongestSubsequence(
        self,
        words: list[str],
        groups: list[int],
    ) -> list[str]:
        if len(words) == 0:
            return []

        result = [words[0]]
        for i in range(1, len(words)):
            if groups[i - 1] != groups[i]:
                result.append(words[i])

        return result


if __name__ == "__main__":
    words = ["e", "a", "b"]
    groups = [0, 0, 1]

    # words = ["d", "g"]
    # groups = [0, 1]

    print(Solution().getLongestSubsequence(words, groups))

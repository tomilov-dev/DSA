from collections import Counter


class Solution:
    def word_score(self, word: str, score: list[int]) -> int:
        return sum([score[ord(c) - ord("a")] for c in word])

    def maxScoreWords(
        self,
        words: list[str],
        letters: list[str],
        score: list[int],
    ) -> int:
        lmap = Counter(letters)

        def dfs(i: int, lmap: Counter):
            if i == len(words):
                return 0

            max_score = dfs(i + 1, lmap)

            word = words[i]
            word_counter = Counter(word)
            if all(lmap[c] >= word_counter[c] for c in word_counter):
                new_lmap = lmap - word_counter
                max_score = max(
                    max_score, self.word_score(word, score) + dfs(i + 1, new_lmap)
                )

            return max_score

        return dfs(0, lmap)


if __name__ == "__main__":
    words = ["dog", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [
        1,
        0,
        9,
        5,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

    print(Solution().maxScoreWords(words, letters, score))

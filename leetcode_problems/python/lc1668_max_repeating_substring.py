class Solution:
    def maxRepeating(
        self,
        sequence: str,
        word: str,
    ) -> int:
        maxi = 0
        for i, chr in enumerate(sequence):
            if chr != word[0]:
                continue

            j = 0
            c = 0
            while i < len(sequence) and sequence[i] == word[j]:
                c += 1
                i += 1
                j += 1
                j = j % len(word)

            maxi = max(maxi, c // len(word))

        return maxi


if __name__ == "__main__":
    sequence = "ababc"
    word = "ab"

    sequence = "ababc"
    word = "ba"

    sequence = "ababc"
    word = "ac"
    print(Solution().maxRepeating(sequence, word))

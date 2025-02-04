class Solution:
    def minimumPushes(self, word: str) -> int:
        index = 1
        remap = 0
        mapping = dict()
        for char in word:
            if char not in mapping:
                remap += 1
                if remap >= 9:
                    index += 1
                    remap = 0
                mapping[char] = index

        count = 0
        for char in word:
            count += mapping[char]
        return count


if __name__ == "__main__":
    word = "xycdefghij"
    print(Solution().minimumPushes(word))

class Solution:
    def diff(self, word: str) -> tuple[int]:
        diff = []
        for index in range(1, len(word)):
            diff.append(ord(word[index]) - ord(word[index - 1]))
        return tuple(diff)

    def oddString(self, words: list[str]) -> str | None:
        diff = [self.diff(word) for word in words]

        map = dict()
        for index in range(len(diff)):
            # odd = all(num % 2 == 1 for num in diff[index])
            # print(odd)
            if diff[index] in map:
                map[diff[index]][0] += 1
                map[diff[index]][1].append(index)

            else:
                map[diff[index]] = [1, [index]]

        for value in map.values():
            if value[0] == 1:
                return words[value[1][0]]


if __name__ == "__main__":
    words = ["adc", "wzy", "abc"]
    print(Solution().oddString(words))

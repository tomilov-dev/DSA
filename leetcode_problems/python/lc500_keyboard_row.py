class Solution:
    def setup_map(self) -> dict[str, int]:
        map = dict()
        map.update({char: 1 for char in "qwertyuiop"})
        map.update({char: 2 for char in "asdfghjkl"})
        map.update({char: 3 for char in "zxcvbnm"})
        return map

    def findWords(self, words: list[str]) -> list[str]:
        map = self.setup_map()

        answer = []
        for word in words:
            prev = map[word[0].lower()]
            add = True
            for char in word[1:]:
                if map[char.lower()] != prev:
                    add = False
                    break

            if add:
                answer.append(word)

        return answer


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))

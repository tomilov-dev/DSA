class Solution:
    def countCharacters(
        self,
        words: list[str],
        chars: str,
    ) -> int:
        charsmap = dict()
        for char in chars:
            charsmap[char] = charsmap.get(char, 0) + 1

        goodwords = 0
        for word in words:
            charmap = charsmap.copy()
            good = True
            for char in word:
                if charmap.get(char, 0) == 0:
                    good = False
                    break
                else:
                    charmap[char] -= 1

            if good:
                goodwords += len(word)

        return goodwords


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(Solution().countCharacters(words, chars))

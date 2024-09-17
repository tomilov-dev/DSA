class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        p1 = 0
        p2 = 0
        for char in word:
            if char == ch:
                break
            p2 += 1

        if p2 == len(word):
            return word

        lword = list(word)
        while p1 < p2:
            lword[p1], lword[p2] = lword[p2], lword[p1]
            p1 += 1
            p2 -= 1

        return "".join(lword)


if __name__ == "__main__":
    word = "abcdefd"
    ch = "d"
    print(Solution().reversePrefix(word, ch))

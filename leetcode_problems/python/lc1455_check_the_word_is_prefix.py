class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        p1 = 0
        p2 = 0
        while p1 < len(sentence) and sentence[p1] == " ":
            p1 += 1

        c = 1
        while p1 < len(sentence):
            while (
                p2 < len(searchWord)
                and p1 < len(sentence)
                and sentence[p1] == searchWord[p2]
            ):
                p1 += 1
                p2 += 1
                if p2 == len(searchWord):
                    return c

            while p1 < len(sentence) and sentence[p1] != " ":
                p1 += 1

            c += 1
            p1 += 1
            p2 = 0

        return -1


if __name__ == "__main__":
    sentence = "i love eating burger"
    searchWord = "burg"
    print(Solution().isPrefixOfWord(sentence, searchWord))

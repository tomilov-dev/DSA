class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sent = []
        ai = 1
        for word in sentence.split(" "):
            if word.lower().startswith(("a", "e", "i", "o", "u")):
                sent.append(word + "ma" + "a" * ai)
            else:
                sent.append(word[1:] + word[0] + "ma" + "a" * ai)
            ai += 1
        return " ".join(sent)


if __name__ == "__main__":
    sentence = "I speak Goat Latin"
    print(Solution().toGoatLatin(sentence))

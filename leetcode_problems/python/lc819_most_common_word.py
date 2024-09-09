class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        sep = set("!?',;. ")
        banned_set = set(banned)
        words = dict()

        word = []
        for char in paragraph.lower():
            if char in sep:
                cword = "".join(word)
                if cword not in banned_set and cword != "":
                    words[cword] = words.get(cword, 0) + 1

                word = []
            else:
                word.append(char)
        else:
            cword = "".join(word)
            if cword not in banned_set:
                words[cword] = words.get(cword, 0) + 1

            word = []

        mword = ""
        mcount = -1
        for word, count in words.items():
            if count > mcount:
                mword = word
                mcount = count

        return mword


if __name__ == "__main__":
    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    print(Solution().mostCommonWord(paragraph, banned))

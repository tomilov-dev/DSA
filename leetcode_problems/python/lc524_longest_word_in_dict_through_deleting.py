class Solution:
    def findLongestWord(
        self,
        s: str,
        dictionary: list[str],
    ) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""


if __name__ == "__main__":
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    print(Solution().findLongestWord(s, dictionary))

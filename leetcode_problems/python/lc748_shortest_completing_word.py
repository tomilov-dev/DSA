class Solution:
    def charc(self, word: str) -> dict[str, int]:
        charc = dict()
        for char in word.lower():
            if char.isalpha():
                charc[char] = charc.get(char, 0) + 1
        return charc

    def shortestCompletingWord(
        self,
        licensePlate: str,
        words: list[str],
    ) -> str:
        licmap = self.charc(licensePlate)
        dicts = [self.charc(w) for w in words]

        minlen = float("inf")
        minword = None
        for index in range(len(words)):
            wlen = len(words[index])
            wdict = dicts[index]
            for char, lfreq in licmap.items():
                wfreq = wdict.get(char, 0)
                if lfreq > wfreq:
                    break
            else:
                if wlen < minlen:
                    minlen = wlen
                    minword = words[index]

        return minword


if __name__ == "__main__":
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    print(Solution().shortestCompletingWord(licensePlate, words))

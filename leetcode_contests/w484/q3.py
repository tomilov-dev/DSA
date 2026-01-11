class Solution:
    def countPairs(self, words: list[str]) -> int:
        total = 0
        mp: dict[int, dict[str, int]] = dict()
        for w in words:
            n = len(w)
            if n in mp:
                for b in range(26):
                    nw = []
                    for c in w:
                        nc = chr((ord(c) - ord("a") + b) % 26 + ord("a"))
                        nw.append(nc)
                    nw = "".join(nw)
                    total += mp[n].get(nw, 0)

            if n not in mp:
                mp[n] = dict()
            mp[n][w] = mp[n].get(w, 0) + 1
        return total


if __name__ == "__main__":
    words = ["fusion", "layout"]
    words = ["ab", "aa", "za", "aa"]
    print(Solution().countPairs(words))

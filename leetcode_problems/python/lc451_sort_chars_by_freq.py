from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        rev_freq: dict[int, list[str]] = dict()
        for char, fq in freq.items():
            if fq not in rev_freq:
                rev_freq[fq] = []
            rev_freq[fq].append(char)

        asc_freq = list(rev_freq.keys())
        asc_freq.sort(reverse=True)

        res = []
        for fq in asc_freq:
            for char in rev_freq[fq]:
                res.extend([char] * fq)
        return "".join(res)


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = [char * count for char, count in sorted_chars]
        return "".join(res)


if __name__ == "__main__":
    s = "tree"
    print(Solution().frequencySort(s))

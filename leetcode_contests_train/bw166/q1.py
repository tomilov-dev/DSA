class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = dict()
        major = dict()
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        maxq = 0
        maxfq = 0
        for c, fq in freq.items():
            if fq not in major:
                major[fq] = []
            major[fq].append(c)
            q = len(major[fq])
            if q > maxq:
                maxq = q
                maxfq = fq
            elif q == maxq and fq > maxfq:
                maxq = q
                maxfq = fq
        return "".join(major[maxfq])


if __name__ == "__main__":
    s = "aaabbbccdddde"
    print(Solution().majorityFrequencyGroup(s))

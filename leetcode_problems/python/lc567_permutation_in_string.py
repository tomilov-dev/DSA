from collections import Counter


class Solution:
    def checkInclusion(
        self,
        s1: str,
        s2: str,
    ) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        freq1, freq2 = Counter(s1), Counter(s2[0:n1])
        if freq1 == freq2:
            return True

        l, r = 0, n1
        while r < n2:
            freq2[s2[l]] -= 1
            freq2[s2[r]] += 1
            if freq1 == freq2:
                return True

            r += 1
            l += 1
        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"

    # s1 = "ab"
    # s2 = "eidboaoo"

    # s1 = "adc"
    # s2 = "dcda"

    print(Solution().checkInclusion(s1, s2))

class Solution:
    def diStringMatch(
        self,
        s: str,
    ) -> list[int]:
        low = 0
        high = len(s)
        perm = []
        for i in range(0, len(s) + 1):
            if i == len(s):
                perm.append(low)
                low += 1
            else:
                if s[i] == "I":
                    perm.append(low)
                    low += 1
                else:
                    perm.append(high)
                    high -= 1

        return perm


if __name__ == "__main__":
    s = "IDID"
    print(Solution().diStringMatch(s))

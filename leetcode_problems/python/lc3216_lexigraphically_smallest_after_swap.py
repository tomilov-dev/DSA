class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s) - 1):
            int1 = int(s[i])
            int2 = int(s[i + 1])
            if int1 % 2 == int2 % 2:
                if int1 > int2:
                    return s[:i] + s[i + 1] + s[i] + s[i + 2 :]

        return s


if __name__ == "__main__":
    s = "45320"
    print(Solution().getSmallestString(s))

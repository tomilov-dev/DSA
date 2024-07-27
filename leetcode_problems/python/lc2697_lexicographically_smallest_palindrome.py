class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        string = list(s)
        index1 = 0
        index2 = len(string) - 1

        while index2 > index1:
            if string[index1] != string[index2]:
                if string[index1] < string[index2]:
                    string[index2] = string[index1]
                else:
                    string[index1] = string[index2]

            index1 += 1
            index2 -= 1

        return "".join(string)


if __name__ == "__main__":
    s = "egcfe"
    print(Solution().makeSmallestPalindrome(s))

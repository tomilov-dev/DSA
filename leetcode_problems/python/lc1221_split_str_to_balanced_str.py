class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cr = 0
        cl = 0

        count = 0
        for char in s:
            if char == "R":
                cr += 1
            else:
                cl += 1

            if cr == cl:
                cr = 0
                cl = 0
                count += 1

        return count


if __name__ == "__main__":
    s = "RLRRLLRLRL"

    print(Solution().balancedStringSplit(s))

class Solution:
    def countKConstraintSubstrings(
        self,
        s: str,
        k: int,
    ) -> int:
        c = 0
        for i in range(len(s)):
            z = 0
            o = 0
            for char in s[i:]:
                z += int(char == "0")
                o += int(char == "1")
                if z > k and o > k:
                    break

                c += 1

        return c


class SolutionSlidingWindow:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        c = 0
        z = 0
        o = 0
        p1 = 0

        for p2 in range(n):
            z += int(s[p2] == "0")
            o += int(s[p2] == "1")

            while z > k and o > k:
                z -= int(s[p1] == "0")
                o -= int(s[p1] == "1")
                p1 += 1

            c += p2 - p1 + 1

        return c


if __name__ == "__main__":
    s = "10101"
    k = 1
    print(Solution().countKConstraintSubstrings(s, k))

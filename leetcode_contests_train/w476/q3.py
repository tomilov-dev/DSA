class Solution:
    def countDistinct(self, n: int) -> int:
        pow9 = [1] * 16
        s = str(n)
        m = len(s)
        ans = 0

        for i in range(1, 16):
            pow9[i] = pow9[i - 1] * 9

        for i in range(1, m):
            ans += pow9[i]

        i = 0
        while i < m:
            if s[i] == "0":
                break
            for _ in range(1, int(s[i])):
                ans += pow9[m - i - 1]
            i += 1

        return ans + (i >= m)


if __name__ == "__main__":
    Solution().countDistinct(100)

class Solution:
    def maximumCostSubstring(
        self,
        s: str,
        chars: str,
        vals: list[int],
    ) -> int:
        alp = "abcdefghijklmnopqrstuvwxyz"
        charmap: dict[str, int] = {char: ord(char) - ord("a") + 1 for char in alp}
        for index, char in enumerate(chars):
            value = vals[index]
            charmap[char] = value

        n = len(s)
        dp = [0] + [charmap[char] for char in s]
        for i in range(1, n + 1):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
        return max(dp)


if __name__ == "__main__":
    s = "adaa"
    chars = "d"
    vals = [-1000]

    s = "kqqqqqkkkq"
    chars = "kq"
    vals = [-6, 6]
    print(Solution().maximumCostSubstring(s, chars, vals))

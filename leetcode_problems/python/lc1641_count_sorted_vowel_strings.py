class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] * n
        dp[0] = ["a", "e", "i", "o", "u"]

        for i in range(1, n):
            storage = []
            for sub in dp[i - 1]:
                for vow in dp[0]:
                    if sub[-1] > vow:
                        continue
                    storage.append(sub + vow)

            dp[i] = storage

        return len(dp[n - 1])


if __name__ == "__main__":
    n = 3
    print(Solution().countVowelStrings(n))

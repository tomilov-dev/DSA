class Solution:
    def countNumbersWithUniqueDigits(
        self,
        n: int,
    ) -> int:
        def backtrack(i: int):
            nonlocal count
            if i >= n:
                return None

            for j in range(0, 10):
                if i == 0 and j == 0:
                    continue
                if used[j]:
                    continue

                count += 1
                used[j] = True
                backtrack(i + 1)
                used[j] = False

        count = 1
        used = [False] * 10
        backtrack(0)
        return count


class SolutionDP:
    def countNumbersWithUniqueDigits(
        self,
        n: int,
    ) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        dp = [1, 10] + [0] * (n - 1)

        unique_digits = 9
        available_numbers = 9
        for i in range(2, n + 1):
            unique_digits *= available_numbers
            dp[i] = dp[i - 1] + unique_digits
            available_numbers -= 1

        return dp[n]


if __name__ == "__main__":
    n = 3
    # print(Solution().countNumbersWithUniqueDigits(n))
    print(SolutionDP().countNumbersWithUniqueDigits(n))

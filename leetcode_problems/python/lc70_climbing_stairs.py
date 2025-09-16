"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


class Solution1:
    """
    Too slow: Runtime Error. Recursive computing with redundant calculations.
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.run(n - 1) + self.run(n - 2)


class Solution2:
    """
    37 ms, 16.2 MB
    """

    def recursion(self, n: int, memo: dict) -> int:
        if n not in memo:
            memo[n] = self.recursion(n - 1, memo) + self.recursion(n - 2, memo)
        return memo[n]

    def run(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        return self.recursion(n, memo)


class Solution3:
    """
    38 ms, 16.2 MB
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [1] * (n + 1)
        for index in range(2, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]

        return dp[n]


class Solution4:
    """
    37 ms, 16.2 MB
    """

    def run(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        curr = 1
        prev = 1
        for _ in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr

class Solution:
    def canEat(
        self,
        candiesCount: list[int],
        queries: list[list[int]],
    ) -> list[bool]:
        n = len(candiesCount)
        answer = []
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = candiesCount[i - 1] + dp[i - 1]

        for candy, day, cap in queries:
            earliest = day + 1
            latest = (day + 1) * cap
            can_eat = dp[candy] < latest and dp[candy + 1] >= earliest
            answer.append(can_eat)
        return answer


if __name__ == "__main__":
    candiesCount = [7, 4, 5, 3, 8]
    queries = [
        [0, 2, 2],
        [4, 2, 4],
        [2, 13, 1000000000],
    ]
    candiesCount = [5, 2, 6, 4, 1]
    queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]
    print(Solution().canEat(candiesCount, queries))

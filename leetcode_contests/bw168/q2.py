class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = [0] * num
        for i in range(num):
            cur = min(9, sum)
            res[i] = cur
            sum -= cur
            if sum == 0:
                break
        if sum > 0:
            return ""
        return "".join([str(x) for x in res])


if __name__ == "__main__":
    num = 2
    sum = 3

    num = 2
    sum = 17

    num = 1
    sum = 10

    sol = Solution()
    print(sol.maxSumOfSquares(num, sum))

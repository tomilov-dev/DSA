class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        return min(e + s for e, s in tasks)


if __name__ == "__main__":
    tasks = [[1, 6], [2, 3]]
    sol = Solution()
    res = sol.earliestTime(tasks)
    print(res)

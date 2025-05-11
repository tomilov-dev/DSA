class Solution:
    def printNos(self, n: int) -> None:
        if n <= 0:
            return None

        print(n, end=" ")
        self.printNos(n - 1)


if __name__ == "__main__":
    n = 5
    Solution().printNos(n)

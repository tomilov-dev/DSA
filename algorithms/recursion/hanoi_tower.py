class Solution:
    def towerOfHanoi(self, n: int) -> int:
        def move(disks: int, source: int, target: int, auxiliary: int) -> int:
            if disks == 0:
                return 0

            steps = move(disks - 1, source, auxiliary, target)
            steps += 1
            steps += move(disks - 1, auxiliary, target, source)
            return steps

        return move(n, 0, 2, 1)


if __name__ == "__main__":
    n = 2
    print(Solution().towerOfHanoi(n))

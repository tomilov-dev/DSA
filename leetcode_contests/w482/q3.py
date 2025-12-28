class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        x = 0
        for l in range(1, k + 1):
            x = (x * 10 + 1) % k
            if x == 0:
                return l
        return -1


if __name__ == "__main__":
    k = 3
    print(Solution().minAllOneMultiple(k))

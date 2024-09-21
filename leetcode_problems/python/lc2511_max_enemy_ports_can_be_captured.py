class Solution:
    def captureForts(self, forts: list[int]) -> int:
        maxi = 0
        n = len(forts)

        for i in range(n):
            if forts[i] == 1:
                j = i - 1
                while j >= 0 and forts[j] == 0:
                    j -= 1
                if j >= 0 and forts[j] == -1:
                    maxi = max(maxi, i - j - 1)

                j = i + 1
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[j] == -1:
                    maxi = max(maxi, j - i - 1)

        return maxi


if __name__ == "__main__":
    forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
    print(Solution().captureForts(forts))

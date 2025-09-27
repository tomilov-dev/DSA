class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def maxh(values: list[int]) -> int:
            index = 0
            lvl = 1
            while values[index] >= lvl:
                values[index] -= lvl
                lvl += 1
                index = (index + 1) % 2
            return lvl - 1

        return max(maxh([red, blue]), maxh([blue, red]))


if __name__ == "__main__":
    red = 2
    blue = 4
    red = 2
    blue = 1
    red = 1
    blue = 1
    red = 10
    blue = 1
    print(Solution().maxHeightOfTriangle(red, blue))

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        index1 = len(colors) - 1
        while index1 >= 0 and colors[index1] == colors[0]:
            index1 -= 1

        index2 = 0
        while index2 < len(colors) and colors[index2] == colors[-1]:
            index2 += 1
        index2 = len(colors) - index2 - 1

        return max(index1, index2)

    def maxDistance2(self, colors: list[int]) -> int:
        max_dist = 0

        for i in range(len(colors)):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, len(colors) - 1 - i)

        return max_dist


if __name__ == "__main__":
    colors = [1, 1, 1, 6, 1, 1, 1]
    colors = [4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]

    print(Solution().maxDistance(colors))

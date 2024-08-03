class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        mall = len(position)
        even = sum(map(lambda x: x % 2 == 0, position))
        res = even if even < mall - even else mall - even
        return res


if __name__ == "__main__":
    position = [2, 2, 2, 3, 3]
    print(Solution().minCostToMoveChips(position))

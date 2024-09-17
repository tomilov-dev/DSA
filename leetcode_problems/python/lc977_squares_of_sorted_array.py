class Solution:
    def sortedSquares(
        self,
        nums: list[int],
    ) -> list[int]:
        p1 = 0
        p2 = len(nums) - 1
        result = []
        while p1 <= p2:
            if p1 == p2:
                result.append(nums[p2] ** 2)
                break

            else:
                if abs(nums[p1]) > nums[p2]:
                    result.append(nums[p1] ** 2)
                    p1 += 1
                else:
                    result.append(nums[p2] ** 2)
                    p2 -= 1

        return list(reversed(result))


if __name__ == "__main__":
    # nums = [-4, -3, -2, -1]
    # nums = [1, 2, 3, 4, 5]
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))

class Solution:
    def twoSum(
        self,
        numbers: list[int],
        target: int,
    ) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            cursum = numbers[p1] + numbers[p2]
            if cursum == target:
                return [p1 + 1, p2 + 1]
            elif cursum > target:
                p2 -= 1
            else:
                p1 += 1

        return [-1, -1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))

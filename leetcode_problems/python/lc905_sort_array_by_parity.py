class Solution:
    def sortArrayByParity(
        self,
        nums: list[int],
    ) -> list[int]:
        odds = []
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        return evens + odds


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(nums))

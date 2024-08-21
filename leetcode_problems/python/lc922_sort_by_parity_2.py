class Solution:
    def sortArrayByParityII(
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

        for index in range(len(nums)):
            if index % 2 == 0:
                nums[index] = evens.pop()
            else:
                nums[index] = odds.pop()

        return nums


if __name__ == "__main__":
    nums = [4, 2, 5, 7]
    print(Solution().sortArrayByParityII(nums))

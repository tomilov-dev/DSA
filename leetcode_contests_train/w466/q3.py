class SolutionBruteForce:
    def bowlSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            length = 1
            maxi = 0
            for j in range(i + 1, n):
                length += 1
                if length >= 3 and min(nums[i], nums[j]) > maxi:
                    total += 1
                maxi = max(maxi, nums[j])
        return total


class SolutionStack:
    def bowlSubarrays(self, nums: list[int]) -> int:
        total = 0
        stack = []
        for num in nums:
            while stack and stack[-1] <= num:
                stack.pop()
                if len(stack) > 0:
                    total += 1
            stack.append(num)
        return total


if __name__ == "__main__":
    nums = [2, 5, 3, 1, 4]
    nums = [5, 1, 2, 3, 4]
    # nums = [1000000000, 999999999, 999999998]
    sol = SolutionBruteForce()
    print(sol.bowlSubarrays(nums))

class Solution1:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return -1
        if n == 2:
            return abs(nums[0] - nums[1])

        incr = 0
        incr_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                incr = i - 1
                break
            incr_sum += nums[i]

        decr_sum = 0
        for i in range(incr + 1, n):
            if nums[i - 1] <= nums[i]:
                return -1
            decr_sum += nums[i]

        result = abs(incr_sum - decr_sum)
        if nums[incr] > nums[i]:
            incr_sum -= nums[incr]
            decr_sum += nums[incr]
            result = min(abs(incr_sum - decr_sum), result)
        return result


class Solution2:
    def splitArray(self, nums: list[int]) -> int:
        def is_incr(arr: list[int]) -> bool:
            return all(arr[j] < arr[j + 1] for j in range(len(arr) - 1))

        def is_decr(arr: list[int]) -> bool:
            return all(arr[j] > arr[j + 1] for j in range(len(arr) - 1))

        n = len(nums)
        results = []
        for i in range(1, n):
            left = nums[:i]
            right = nums[i:]
            if is_incr(left) and is_decr(right):
                diff = abs(sum(left) - sum(right))
                results.append(diff)

        return min(results) if results else -1


if __name__ == "__main__":
    nums = [1, 2, 4, 3]
    nums = [1, 3, 2]
    nums = [3, 1, 2]
    nums = [2, 2]
    print(Solution2().splitArray(nums))

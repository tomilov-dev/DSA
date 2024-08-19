class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [0 for _ in range(10)]

        nums1 = []
        nums2 = []

        rem = num
        while rem > 0:
            nums[rem % 10] += 1
            rem //= 10

        for number in range(len(nums)):
            numc = nums[number]
            while numc > 0:
                if len(nums1) > len(nums2):
                    nums2.append(number)
                else:
                    nums1.append(number)

                numc -= 1

        return int("".join([str(x) for x in nums1])) + int(
            "".join([str(x) for x in nums2])
        )


if __name__ == "__main__":
    num = 2932
    print(Solution().minimumSum(num))

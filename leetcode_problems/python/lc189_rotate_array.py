class Solution:
    def rotate_sub_array(
        self,
        nums: list[int],
        i: int,
        j: int,
    ) -> None:
        j -= 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        # 1. Полностью разворачиваем массив
        self.rotate_sub_array(nums, 0, n)
        # 2. Разворачиваем 0..k подмассив
        self.rotate_sub_array(nums, 0, k)
        # 3. Разворачиваем k..n подмассив
        self.rotate_sub_array(nums, k, n)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().rotate(nums, k))

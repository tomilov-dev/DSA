class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix = self.build_prefix(nums)
        print(self.prefix)

    def build_prefix(self, nums: list[int]) -> list[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        return prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    numarr = NumArray([-2, 0, 3, -5, 2, -1])
    print(numarr.sumRange(0, 2))

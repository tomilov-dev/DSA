from utils import TreeNode


class KthLargest:
    def __init__(
        self,
        k: int,
        nums: list[int],
    ):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]

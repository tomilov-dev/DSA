import random


class Solution:
    def quick_select(
        self,
        values: list[tuple[int, int]],
        k: int,
    ) -> list[tuple[int, int]]:
        if not values:
            return

        x = random.choice(values)
        xv = x[1]

        left = [v for v in values if v[1] > xv]
        mid = [v for v in values if v[1] == xv]
        right = [v for v in values if v[1] < xv]

        if k < len(left):
            return self.quick_select(left, k)
        elif k > len(left) + len(mid):
            return left + mid + self.quick_select(right, k - len(left) - len(mid))
        else:
            return left + mid[: k - len(left)]

    def topKFrequent(
        self,
        nums: list[int],
        k: int,
    ) -> list[int]:
        mem = dict()
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1

        numz = [(k, v) for k, v in mem.items()]
        result = self.quick_select(numz, k)
        if result:
            return [v[0] for v in result]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    res = Solution().topKFrequent(nums, k)
    print(res)

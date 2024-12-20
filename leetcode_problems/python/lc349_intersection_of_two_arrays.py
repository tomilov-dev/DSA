class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))


class Solution2:
    def intersection(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[int]:
        nset = set(nums1)
        result = []
        for num in set(nums2):
            if num in nset:
                result.append(num)
        return result


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution2().intersection(nums1, nums2))

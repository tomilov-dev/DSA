class Solution:
    def intersection(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[int]:
        p1 = 0
        p2 = 0

        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return result


if __name__ == "__main__":
    nums1 = [1, 2, 3, 3, 4, 5, 6]
    nums2 = [3, 3, 5]
    print(Solution().intersection(nums1, nums2))

class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        merged = dict()
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                merged[nums1[i][0]] = merged.get(nums1[i][0], 0) + nums1[i][1]
            if i < len(nums2):
                merged[nums2[i][0]] = merged.get(nums2[i][0], 0) + nums2[i][1]

        return sorted([[k, v] for k, v in merged.items()])


if __name__ == "__main__":
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    print(Solution().mergeArrays(nums1, nums2))

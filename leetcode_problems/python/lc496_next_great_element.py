class Solution:
    def nextGreaterElement(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[int] | None:
        if not nums2:
            return None

        map = dict()
        stack = [nums2[0]]
        for index in range(1, len(nums2)):
            while stack and stack[-1] < nums2[index]:
                map[stack.pop()] = nums2[index]
            stack.append(nums2[index])

        return [map.get(num, -1) for num in nums1]


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))

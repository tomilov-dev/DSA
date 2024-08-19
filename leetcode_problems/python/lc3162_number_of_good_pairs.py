class Solution:
    def numberOfPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        k: int,
    ) -> int:
        count = 0
        map = dict()

        for num in nums2:
            if num * k not in map:
                map[num * k] = 1
            else:
                map[num * k] += 1

        for num in nums1:
            for div in map:
                if num % div == 0:
                    count += map[div]

        return count


if __name__ == "__main__":
    nums1 = [1, 3, 4]
    nums2 = [1, 3, 4]
    k = 1

    print(Solution().numberOfPairs(nums1, nums2, k))

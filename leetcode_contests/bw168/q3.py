class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        minx = 10**6
        res = 0
        n = len(nums1)

        t = nums2[n]
        for i in range(n):
            x = nums1[i]
            y = nums2[i]

            s1 = abs(nums2[n] - x)
            s2 = abs(nums2[n] - y)
            minx = min(minx, s1, s2)
            if x < y and x <= t <= y:
                minx = 0
            elif x >= y and y <= t <= x:
                minx = 0
            res += abs(x - y)

        return res + abs(minx) + 1


if __name__ == "__main__":

    nums1 = [2, 8]
    nums2 = [1, 7, 3]

    # nums1 = [1, 3, 6]
    # nums2 = [2, 4, 5, 3]

    # nums1 = [2]
    # nums2 = [3, 4]

    # nums1 = [458, 915]
    # nums2 = [709, 596, 318]

    # nums1 = [753, 357]
    # nums2 = [271, 520, 413]

    sol = Solution()
    print(sol.minOperations(nums1, nums2))

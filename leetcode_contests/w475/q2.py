class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        ilast = {}
        imid = {}
        mini = 10**10
        for idx, num in enumerate(nums):
            if num in imid:
                dist = (
                    abs(imid[num] - ilast[num])
                    + abs(ilast[num] - idx)
                    + abs(idx - imid[num])
                )
                mini = min(mini, dist)
            if num in ilast:
                imid[num] = ilast[num]
            ilast[num] = idx

        return mini if mini != 10**10 else -1


if __name__ == "__main__":

    sol = Solution()
    res = sol.minimumDistance([1, 2, 1, 1, 3])
    res = sol.minimumDistance([1, 1, 2, 3, 2, 1, 2])
    print(res)

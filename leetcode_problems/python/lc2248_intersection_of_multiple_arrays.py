class Solution:
    def intersection(
        self,
        nums: list[list[int]],
    ) -> list[int]:
        arrs_len = [len(arr) for arr in nums]
        min_arr_index = arrs_len.index(min(arrs_len))

        sets = [set(arr) for arr in nums]
        intersect = sets[min_arr_index]
        for index in range(len(sets)):
            if index == min_arr_index:
                continue

            set_ = sets[index]
            intersect.intersection_update(set_)

        return sorted(intersect)


if __name__ == "__main__":
    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    print(Solution().intersection(nums))

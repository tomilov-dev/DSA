class SolutionHashTable:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        mem = set()
        for i, j in nums:
            for k in range(i, j + 1):
                mem.add(k)
        return len(mem)


class SolutionInterval:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort(key=lambda x: (x[0], x[1]))
        total = 0
        current_end = -1
        for start, end in nums:
            if start > current_end:
                total += end - start + 1
            else:
                total += max(end - current_end, 0)
            current_end = max(current_end, end)
        return total


if __name__ == "__main__":
    nums = [[3, 6], [1, 5], [4, 7]]
    nums = [[1, 3], [5, 8]]
    sol = SolutionInterval()
    print(sol.numberOfPoints(nums))

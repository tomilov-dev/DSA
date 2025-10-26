from collections import defaultdict
import bisect


class Solution:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + capacity[i - 1]

        res = 0
        for i in range(n):
            for j in range(i + 2, n):
                n1 = capacity[i]
                n2 = capacity[j]
                n3 = pref[j] - pref[i + 1]
                if n1 == n2 == n3:
                    res += 1

        return res


class SolutionOptimized:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + capacity[i - 1]

        index: dict[int, list[int]] = dict()
        for i, val in enumerate(capacity):
            if val not in index:
                index[val] = []
            index[val].append(i)

        res = 0
        for value in index:
            m = len(index[value])
            if m < 2:
                continue

            for i in range(m):
                for j in range(m - 1, i, -1):
                    start = index[value][i]
                    end = index[value][j]
                    if end - start < 2:
                        break
                    if pref[end] - pref[start + 1] == value:
                        res += 1

        return res


class SolutionOptimized2:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + capacity[i - 1]

        index: dict[int, list[int]] = dict()
        for i, v in enumerate(capacity):
            if v not in index:
                index[v] = []
            index[v].append(i)

        res = 0
        for left in range(n - 2):
            value = capacity[left]
            target_sum = pref[left + 1] + value
            indexes = index[value]
            pos = bisect.bisect_right(indexes, left + 1)
            for right in indexes[pos:]:
                if pref[right] == target_sum:
                    res += 1
        return res


if __name__ == "__main__":
    capacity = [9, 3, 3, 3, 9]
    capacity = [1, 2, 3, 4, 5]
    capacity = [-4, 4, 0, 0, -8, -4]
    capacity = [0, 0, 0, 0]
    sol = Solution()
    sol = SolutionOptimized()
    sol = SolutionOptimized2()
    print(sol.countStableSubarrays(capacity))

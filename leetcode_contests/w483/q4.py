import heapq
from functools import lru_cache
from itertools import combinations


class SolutionWrong:
    def minMergeCost(self, lists: list[list[int]]) -> int:
        def md(arr: list[int]) -> int:
            return arr[(len(arr) - 1) // 2]

        def merge(a: list[int], b: list[int]) -> list[int]:
            merged = []
            ia, ib = 0, 0
            while ia < len(a) and ib < len(b):
                if a[ia] < b[ib]:
                    merged.append(a[ia])
                    ia += 1
                else:
                    merged.append(b[ib])
                    ib += 1
            merged.extend(a[ia:])
            merged.extend(b[ib:])
            return merged

        total_cost = 0
        while len(lists) > 1:
            heap = []
            for i in range(len(lists)):
                for j in range(i + 1, len(lists)):
                    a, b = lists[i], lists[j]
                    cost = len(a) + len(b) + abs(md(a) - md(b))
                    heapq.heappush(heap, (cost, i, j))
            cost, i, j = heapq.heappop(heap)
            merged = merge(lists[i], lists[j])
            lists.pop(max(i, j))
            lists.pop(min(i, j))
            lists.append(merged)
            total_cost += cost
        return total_cost


class Solution:
    def minMergeCost(self, lists: list[list[int]]) -> int:
        def md(arr: list[int]) -> int:
            return arr[(len(arr) - 1) // 2]

        def merge(a: list[int], b: list[int]) -> list[int]:
            merged = []
            ia, ib = 0, 0
            while ia < len(a) and ib < len(b):
                if a[ia] < b[ib]:
                    merged.append(a[ia])
                    ia += 1
                else:
                    merged.append(b[ib])
                    ib += 1
            merged.extend(a[ia:])
            merged.extend(b[ib:])
            return merged

        @lru_cache(maxsize=None)
        def dp(state):
            if len(state) == 1:
                return 0
            res = MAX
            for i, j in combinations(range(len(state)), 2):
                a, b = state[i], state[j]
                merged = merge(a, b)
                cost = len(a) + len(b) + abs(md(a) - md(b))
                new_state = []
                for k in range(len(state)):
                    if k != i and k != j:
                        new_state.append(state[k])
                new_state.append(tuple(merged))
                res = min(res, dp(tuple(sorted(new_state))) + cost)
            return res

        MAX = 10**10
        start = tuple(tuple(lst) for lst in lists)
        return dp(start)


if __name__ == "__main__":
    print(Solution().minMergeCost([[1, 3, 5], [2, 4], [6, 7, 8]]))
    print(Solution().minMergeCost([[1, 1, 5], [1, 4, 7, 8]]))
    print(Solution().minMergeCost([[1], [3]]))
    print(Solution().minMergeCost([[1], [1]]))
    print(Solution().minMergeCost([[7, 10, 10], [4], [2, 6, 10]]))

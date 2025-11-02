from functools import lru_cache


class SolutionRecursive:
    def minimumTime(
        self,
        d: list[int],
        r: list[int],
    ) -> int:
        @lru_cache(maxsize=None)
        def rec(c1: int, c2: int, time: int) -> int:
            if c1 >= d1 and c2 >= d2:
                return time

            mini = 10**12
            done = False
            if c1 < d1 and time % r1 != 0:
                mini = min(mini, rec(c1 + 1, c2, time + 1))
                done = True
            if c2 < d2 and time % r2 != 0:
                mini = min(mini, rec(c1, c2 + 1, time + 1))
                done = True
            if not done:
                mini = min(mini, rec(c1, c2, time + 1))
            return mini

        d1, d2 = d
        r1, r2 = r
        return rec(0, 0, 1) - 1


class SolutionOld:
    def minimumTime(
        self,
        d: list[int],
        r: list[int],
    ) -> int:
        d1, d2 = d
        r1, r2 = r
        cx = [[0, 0], [0, 0]]
        time = 0
        while True:
            time += 1
            # option 1 - consider add 1-st
            if cx[0][0] < d1 and time % r1 != 0:
                cx[0][0] += 1
            elif cx[0][1] < d2 and time % r2 != 0:
                cx[0][1] += 1

            if cx[0][0] >= d1 and cx[0][1] >= d2:
                break

            # option 2 - consider add 2-nd
            if cx[1][1] < d2 and time % r2 != 0:
                cx[1][1] += 1
            elif cx[1][0] < d1 and time % r1 != 0:
                cx[1][0] += 1

            if cx[1][0] >= d1 and cx[1][1] >= d2:
                break

        return time


class Solution:
    def minimumTime(self, d: list[int], r: list[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        def enough(T):
            a = T - T // r1
            b = T - T // r2
            return a >= d1 and b >= d2 and a + b >= d1 + d2

        left, right = 1, (d1 + d2) * max(r1, r2)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if enough(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer


if __name__ == "__main__":
    d = [3, 1]
    r = [2, 3]

    d = [1, 3]
    r = [2, 2]

    d = [2, 1]
    r = [3, 4]

    d = [1, 1]
    r = [3, 2]

    d = [906691060, 413654000]
    r = [24838, 29173]

    sol = Solution()
    print(sol.minimumTime(d, r))

from functools import lru_cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count(x: int) -> int:
            s = str(x)
            n = len(s)

            @lru_cache(maxsize=None)
            def dp(
                pos: int,
                diff: int,
                tight: bool,
                leading_zero: bool,
                length: int,
            ):
                if pos == n:
                    return int(length >= 2 and diff == 0)
                res = 0
                up = int(s[pos]) if tight else 9
                for d in range(0, up + 1):
                    next_tight = tight and (d == up)
                    next_leading_zero = leading_zero and (d == 0)
                    next_length = length if next_leading_zero else length + 1
                    if next_leading_zero:
                        res += dp(pos + 1, diff, next_tight, True, length)
                    else:
                        pos_in_num = next_length
                        if pos_in_num % 2 == 1:
                            res += dp(pos + 1, diff + d, next_tight, False, next_length)
                        else:
                            res += dp(pos + 1, diff - d, next_tight, False, next_length)
                return res

            return dp(0, 0, True, True, 0)

        return count(high) - count(low - 1)


if __name__ == "__main__":
    low = 1
    high = 100
    print(Solution().countBalanced(low, high))

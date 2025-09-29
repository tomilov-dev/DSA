class SolutionRecusrive:
    def longestSubsequence(self, s: str, k: int) -> int:
        def rec(i: int, l: int, sum_: int) -> int:
            if sum_ > k:
                return -1
            if i < 0:
                return l

            to_add = rec(i - 1, l + 1, sum_ + int(s[i]) * (2**l))
            not_add = rec(i - 1, l, sum_)
            return max(to_add, not_add)

        n = len(s)
        return rec(n - 1, 0, 0)


class SolutionTopDown:
    def longestSubsequence(self, s: str, k: int) -> int:
        def rec(i: int, sum_: int) -> int:
            if sum_ > k:
                return -1
            if i < 0:
                return 0

            key = (i, sum_)
            if key not in mem:
                add = 1 + rec(i - 1, sum_ + int(s[i]) * (1 << (n - 1 - i)))
                not_add = rec(i - 1, sum_)
                mem[key] = max(not_add, add)
            return mem[key]

        n = len(s)
        mem = {}
        return rec(n - 1, 0)


class SolutionBottomUp:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (k + 1)

        for i in range(n):
            digit = int(s[i])
            prev_dp = dp[:]
            for sum_ in range(k + 1):
                new_sum = sum_ + digit * (1 << (n - 1 - i))
                if new_sum <= k:
                    dp[new_sum] = max(dp[new_sum], prev_dp[sum_] + 1)
        return max(dp)


class SolutionGreedy:
    def longestSubsequence(self, s: str, k: int) -> int:
        total = 0
        count = 0
        pw = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            add = 1 * (2**pw)
            if total + add > k:
                break
            if s[i] == "1":
                total += add
                count += 1
            pw += 1

        return s.count("0") + count


if __name__ == "__main__":
    s = "1001010"
    k = 5
    sol = SolutionGreedy()
    print(sol.longestSubsequence(s, k))

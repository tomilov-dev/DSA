class Solution:
    def longestBalanced(self, s: str) -> int:
        def balanced(mem: list[int]) -> bool:
            cache = set(c for c in mem if c > 0)
            return len(cache) <= 1

        def rec(i: int) -> int:
            if i >= n:
                if balanced(mem):
                    return sum(mem)
                return 0

            ind = ord(s[i]) - ord("a")
            mem[ind] += 1
            to_add = rec(i + 1)
            mem[ind] -= 1
            not_add = rec(i + 1)
            return max(to_add, not_add)

        n = len(s)
        mem = [0] * 26
        return rec(0)


if __name__ == "__main__":
    s = "abbac"
    s = "zzabccy"
    print(Solution().longestBalanced(s))

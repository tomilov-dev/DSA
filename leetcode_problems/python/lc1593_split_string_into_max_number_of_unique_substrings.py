class SolutionWrong:
    def maxUniqueSplit(self, s: str) -> int:
        uniq: set[str] = set()
        i = 0
        sub = ""
        while i < len(s):
            sub += s[i]
            if sub not in uniq:
                uniq.add(sub)
                sub = ""
            i += 1
        return len(uniq)


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(i: int, uniq: set[str]) -> int:
            if i == len(s):
                return len(uniq)

            max_count = 0
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub not in uniq:
                    uniq.add(sub)
                    max_count = max(max_count, backtrack(j, uniq))
                    uniq.remove(sub)
            return max_count

        return backtrack(0, set())


if __name__ == "__main__":
    s = "www z f v e d w fv h s ww"
    s = "wwwzfvedwfvhsww"
    # s = "ababccc"
    print(Solution().maxUniqueSplit(s))

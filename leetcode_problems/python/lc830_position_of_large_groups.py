class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        if len(s) < 3:
            return []

        res = []
        start = 0
        for end in range(1, len(s)):
            if s[start] == s[end]:
                continue

            size = end - start
            if size >= 3:
                res.append([start, end - 1])
            start = end
        else:
            size = end - start + 1
            if size >= 3:
                res.append([start, end])
            start = end

        return res


class SolutionWhile:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        n = len(s)
        start = 0
        while start < n:
            end = start
            while end < n and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                res.append([start, end - 1])
            start = end
        return res


if __name__ == "__main__":
    s = "abbxxxxzzy"
    s = "abc"
    s = "abcdddeeeeaabbbcd"
    s = "aaa"
    print(SolutionWhile().largeGroupPositions(s))

from collections import defaultdict


class Solution:
    def groupAnagrams(
        self,
        strs: list[str],
    ) -> list[list[str]]:
        resmap: dict[str, list[str]] = dict()
        for s in strs:
            prep = "".join(sorted(s))
            if prep not in resmap:
                resmap[prep] = []
            resmap[prep].append(s)
        return [v for _, v in resmap.items()]


class Solution:
    def groupAnagrams(
        self,
        strs: list[str],
    ) -> list[list[str]]:
        resmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            resmap[tuple(count)].append(s)
        return resmap.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

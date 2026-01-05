from collections import defaultdict
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = set()
        first = defaultdict(list)
        last = defaultdict(list)
        for w in words:
            first[w[0]].append(w)
            last[w[3]].append(w)

        for top in words:
            for left in first[top[0]]:
                if left == top:
                    continue
                for right in first[top[3]]:
                    if right == top or right == left:
                        continue
                    for bottom in last[right[3]]:
                        if bottom in (top, left, right):
                            continue
                        if bottom[0] == left[3]:
                            res.add(tuple([top, left, right, bottom]))
        return [list(t) for t in sorted(res)]


if __name__ == "__main__":
    print(Solution().wordSquares(["able", "area", "echo", "also"]))

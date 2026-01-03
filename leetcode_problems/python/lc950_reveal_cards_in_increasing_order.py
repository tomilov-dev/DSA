from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        q = deque([])
        for x in sorted(deck)[::-1]:
            q.rotate()
            q.appendleft(x)
        return list(q)

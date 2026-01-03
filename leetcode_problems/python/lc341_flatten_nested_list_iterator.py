class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


from collections import deque


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]) -> None:
        self.q = deque([])
        self._process(nestedList)

    def _process(self, l: list[NestedInteger]) -> None:
        for node in l:
            if node.isInteger():
                self.q.append(node.getInteger())
            else:
                self._process(node.getList())

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) > 0

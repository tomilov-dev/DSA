from typing import List
from pprint import pprint


class Node:
    def __init__(
        self,
        val: int,
        isLeaf: bool,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def create(
        self,
        grid: List[List[int]],
        cmin: int,
        cmax: int,
        rmin: int,
        rmax: int,
    ) -> Node:
        cspread = cmax - cmin
        rspread = rmax - rmin
        if cspread <= 1 or rspread <= 1:
            return Node(grid[cmin][rmin], True, None, None, None, None)

        cmid = cmin + (cmax - cmin) // 2
        rmid = rmin + (rmax - rmin) // 2

        tl = self.create(grid, cmin, cmid, rmin, rmid)
        tr = self.create(grid, cmin, cmid, rmid, rmax)
        bl = self.create(grid, cmid, cmax, rmin, rmid)
        br = self.create(grid, cmid, cmax, rmid, rmax)

        check1 = tl.isLeaf == tr.isLeaf == bl.isLeaf == br.isLeaf == True
        check2 = tl.val == tr.val == bl.val == br.val
        if check1 and check2:
            node = Node(tl.val, True, None, None, None, None)

        else:
            node = Node(0, False, tl, tr, bl, br)

        return node

    def construct(
        self,
        grid: List[List[int]],
    ) -> "Node":
        return self.create(
            grid,
            cmin=0,
            cmax=len(grid),
            rmin=0,
            rmax=len(grid),
        )


if __name__ == "__main__":
    sol = Solution()

    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]

    quad_tree = sol.construct(grid)

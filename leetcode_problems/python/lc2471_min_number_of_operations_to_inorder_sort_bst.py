from collections import deque
from utils import TreeNode
from utils import build_tree


class Solution:
    def count(self, nums: list[int]) -> int:
        n = len(nums)
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][1] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][1]
                cycle_size += 1

            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps

    def minimumOperations(
        self,
        root: TreeNode | None,
    ) -> int:
        if not root:
            return 0

        q = deque([root])
        order = []
        while q:
            lvl = len(q)
            stack = []
            for _ in range(lvl):
                node = q.popleft()
                stack.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            order.append(stack)

        count = 0
        for sub in order:
            count += self.count(sub)
        return count


if __name__ == "__main__":
    arr = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
    root = build_tree(arr)
    print(Solution().minimumOperations(root))

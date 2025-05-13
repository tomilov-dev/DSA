from collections import deque


class SolutionRecursive:
    def rev(self, q: deque[int]) -> None:
        if not q:
            return None

        k = q.popleft()
        self.reverseQueue(q)
        q.append(k)

    def reverseQueue(self, q: deque[int]) -> deque[int]:
        self.rev(q)
        return q


class SolutionIterative:
    def reverseQueue(self, q: deque[int]) -> deque[int]:
        for i in range(len(q) // 2):
            j = len(q) - i - 1
            q[i], q[j] = q[j], q[i]
        return q


if __name__ == "__main__":
    q = deque([4, 3, 1, 10, 2, 6])
    SolutionRecursive().reverseQueue(q)
    SolutionIterative().reverseQueue(q)

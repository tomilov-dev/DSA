from collections import deque


class DataStream:
    def __init__(self, value: int, k: int):
        self.q = deque([])
        self.v = value
        self.k = k

        self.sum = 0

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num == self.v:
            self.sum += 1
        if len(self.q) > self.k:
            x = self.q.popleft()
            if x == self.v:
                self.sum -= 1
        return self.sum == self.k


class DataStreamWithotQueue:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.state = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.state += 1
        else:
            self.state = 0
        res = True if self.state == self.k else False
        if self.state == self.k:
            self.state -= 1
        return res

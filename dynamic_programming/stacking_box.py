class SolutionRecursive:
    def maxHeight(
        self,
        height: list[int],
        width: list[int],
        length: list[int],
    ) -> int:
        def rec(i: int):
            res = boxes[i][2]
            for j in range(i + 1, len(boxes)):
                if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                    res = max(res, boxes[i][2] + rec(j))
            return res

        boxes = []
        for i in range(len(height)):
            a = height[i]
            b = width[i]
            c = length[i]

            boxes.append([a, b, c])
            boxes.append([a, c, b])
            boxes.append([b, a, c])
            boxes.append([b, c, a])
            boxes.append([c, a, b])
            boxes.append([c, b, a])
        boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)

        n = len(boxes)
        res = 0
        for i in range(n):
            res = max(res, rec(i))
        return res


class SolutionTopDown:
    def maxHeight(
        self,
        height: list[int],
        width: list[int],
        length: list[int],
    ) -> int:
        def rec(i: int):
            if i not in mem:
                mem[i] = 0
                res = boxes[i][2]
                for j in range(i + 1, len(boxes)):
                    if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                        res = max(res, boxes[i][2] + rec(j))
                mem[i] = res
            return mem[i]

        boxes = []
        for i in range(len(height)):
            a = height[i]
            b = width[i]
            c = length[i]

            boxes.append([a, b, c])
            boxes.append([a, c, b])
            boxes.append([b, a, c])
            boxes.append([b, c, a])
            boxes.append([c, a, b])
            boxes.append([c, b, a])
        boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)

        n = len(boxes)
        mem = {}
        res = 0
        for i in range(n):
            res = max(res, rec(i))
        return res


class SolutionBottomUp:
    def maxHeight(
        self,
        height: list[int],
        width: list[int],
        length: list[int],
    ) -> int:
        boxes = []
        for i in range(len(height)):
            a = height[i]
            b = width[i]
            c = length[i]

            boxes.append([a, b, c])
            boxes.append([a, c, b])
            boxes.append([b, a, c])
            boxes.append([b, c, a])
            boxes.append([c, a, b])
            boxes.append([c, b, a])
        boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)

        n = len(boxes)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = boxes[i][2]
            for j in range(i + 1, n):
                if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                    dp[i] = max(dp[i], boxes[i][2] + dp[j])
        return max(dp)


if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]
    print(SolutionRecursive().maxHeight(height, width, length))
    print(SolutionTopDown().maxHeight(height, width, length))
    print(SolutionBottomUp().maxHeight(height, width, length))

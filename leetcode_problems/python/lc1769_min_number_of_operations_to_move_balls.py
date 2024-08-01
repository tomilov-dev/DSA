class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        moves = [0] * len(boxes)

        for i in range(len(moves)):
            move = 0
            for j in range(len(moves)):
                cnt = abs(int(j) - int(i)) * int(boxes[j])
                move += cnt

            moves[i] += move

        return moves


if __name__ == "__main__":
    boxes = "110"
    print(Solution().minOperations(boxes))

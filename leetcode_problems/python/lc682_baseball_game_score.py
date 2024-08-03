class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                scores.append(sum(scores[-2:]))
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))

        return sum(scores)


if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    print(Solution().calPoints(ops))

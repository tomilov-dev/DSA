class Solution:
    def dailyTemperatures(
        self,
        temperatures: list[int],
    ) -> list[int]:
        result = [0 for _ in range(len(temperatures))]
        stack: list[tuple[int, int]] = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                target, _ = stack.pop()
                result[target] = index - target
            stack.append((index, temp))
        return result


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))

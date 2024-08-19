class Solution:
    def minimumBoxes(
        self,
        apple: list[int],
        capacity: list[int],
    ) -> int:
        apples = sum(apple)
        if apples <= 0:
            return 0

        capacity.sort(reverse=True)

        index = 0
        while index < len(capacity) and apples > 0:
            apples -= capacity[index]
            index += 1

        return index


if __name__ == "__main__":
    apple = [1, 3, 2]
    capacity = [4, 3, 1, 5, 2]

    apple = [5, 5, 5]
    capacity = [2, 4, 2, 7]

    print(Solution().minimumBoxes(apple, capacity))

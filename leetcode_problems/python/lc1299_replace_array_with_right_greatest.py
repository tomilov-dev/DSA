class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right = [arr[-1]]

        index = len(arr) - 2
        while index >= 0:
            maxi = max(right[len(right) - 1], arr[index])
            right.append(maxi)
            index -= 1

        right.pop()
        right.reverse()
        right.append(-1)

        return right

    def optimized(self, arr: list[int]) -> list[int]:
        maxi = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = maxi
            maxi = max(maxi, current)
        return arr


if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    print(Solution().replaceElements(arr))

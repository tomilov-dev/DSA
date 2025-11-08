class PrevPermutation:
    def left_bigger(self, arr: list[int]) -> int:
        n = len(arr)
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                return i - 1
        return -1

    def right_smaller(self, arr: list[int], left: int) -> int:
        n = len(arr)
        for i in range(n - 1, left, -1):
            if arr[i] < arr[left]:
                return i
        return -1

    def reverse_tail(self, arr: list[int], ifrom: int) -> list[int]:
        p1 = ifrom
        p2 = len(arr) - 1
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
        return arr

    def run(self, arr: list[int]) -> list[int]:
        left = self.left_bigger(arr)
        if left == -1:
            return arr  # Уже минимальная перестановка

        right = self.right_smaller(arr, left)
        arr[left], arr[right] = arr[right], arr[left]
        return self.reverse_tail(arr, left + 1)


if __name__ == "__main__":
    res = PrevPermutation().run([1, 2, 4, 3, 5, 6])
    print(res)  # [1, 2, 3, 6, 5, 4]

class Solution:
    def transform(self, arr: list[int]) -> list[int]:
        return [(arr[i] + arr[i - 1]) % 10 for i in range(1, len(arr))]

    def hasSameDigits(self, s: str) -> bool:
        arr = [int(x) for x in s]
        while len(arr) > 2:
            arr = self.transform(arr)
        return arr[0] == arr[1]


class SolutionOptimal:
    def transform(self, arr: list[int], stop: int):
        for i in range(stop):
            arr[i] = (arr[i] + arr[i + 1]) % 10

    def hasSameDigits(self, s: str) -> bool:
        arr = [int(x) for x in s]
        for stop in range(len(arr) - 1, 1, -1):
            self.transform(arr, stop)
        return arr[0] == arr[1]


if __name__ == "__main__":
    s = "3902"
    print(SolutionOptimal().hasSameDigits(s))

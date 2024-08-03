class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        indexes = []
        for index in range(len(s)):
            if s[index] == c:
                indexes.append(index)

        answer = []
        j = 0
        for i in range(len(s)):
            min1 = abs(i - indexes[j])
            min2 = abs(i - indexes[min(j + 1, len(indexes) - 1)])
            min3 = abs(i - indexes[max(j - 1, 0)])
            answer.append(min(min1, min2, min3))

            if j != len(indexes) - 1 and indexes[j] == i:
                j += 1

        return answer

    def optimized(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float("inf")] * n

        prev = float("-inf")
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        prev = float("inf")
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer


if __name__ == "__main__":
    s = "loveleetcode"
    c = "e"

    print(Solution().shortestToChar(s, c))

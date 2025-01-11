class Solution:
    def hIndex(
        self,
        citations: list[int],
    ) -> int:
        count = [0] * 1001
        for c in citations:
            count[c] += 1

        index = 0
        for i, c in enumerate(count):
            for _ in range(c):
                citations[index] = i
                index += 1
        citations = citations[::-1]

        h_index = 0
        for i, c in enumerate(citations):
            if i < c:
                h_index = i + 1
            else:
                break
        return h_index


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(Solution().hIndex(citations))

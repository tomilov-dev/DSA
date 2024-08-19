class Solution:
    def answerQueries(
        self,
        nums: list[int],
        queries: list[int],
    ) -> list[int]:
        nums.sort()
        queries_index = sorted((q, i) for i, q in enumerate(queries))

        answer = [0] * len(queries)

        ni = 0
        curlen = 0
        total_sum = 0

        for query, qi in queries_index:
            while ni < len(nums) and total_sum + nums[ni] <= query:
                total_sum += nums[ni]
                curlen += 1
                ni += 1
            answer[qi] = curlen

        return answer


if __name__ == "__main__":
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    # queries = [1, 1, 1]

    # nums = [2, 3, 4, 5]
    # queries = [1]

    print(Solution().answerQueries(nums, queries))

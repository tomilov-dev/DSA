class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sm = 0
        for num, fq in freq.items():
            if fq % k == 0:
                sm += num * fq
        return sm


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3, 3, 4]
    k = 2
    print(Solution().sumDivisibleByK(nums, k))

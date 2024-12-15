class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]
        max_alt = 0
        for num in gain:
            cur_alt = alt[-1] + num
            max_alt = max(max_alt, cur_alt)
            alt.append(cur_alt)

        return max_alt


if __name__ == "__main__":
    gain = [-5, 1, 5, 0, -7]
    print(Solution().largestAltitude(gain))

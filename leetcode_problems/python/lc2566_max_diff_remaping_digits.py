class Solution:
    def minMaxDifference(self, num: int) -> int:
        snum = list(str(num))

        max_num = snum[:]
        for i in range(len(max_num)):
            if max_num[i] != "9":
                replace_digit = max_num[i]
                max_num = [ch if ch != replace_digit else "9" for ch in max_num]
                break

        min_num = snum[:]
        for i in range(len(min_num)):
            if min_num[i] != "0":
                replace_digit = min_num[i]
                min_num = [ch if ch != replace_digit else "0" for ch in min_num]
                break

        max_num = int("".join(max_num))
        min_num = int("".join(min_num))
        return max_num - min_num


if __name__ == "__main__":
    num = 11891
    num = 90

    print(Solution().minMaxDifference(num))

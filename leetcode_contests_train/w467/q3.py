from collections import defaultdict


class SolutionBruteForceDP:
    def subsequenceSumAfterCapping(
        self,
        nums: list[int],
        k: int,
    ) -> list[bool]:
        def capped(x: int) -> list[int]:
            return [min(num, x) for num in nums]

        def subSumIsK(nums: list[int], k: int) -> bool:
            dp = [False] * (k + 1)
            dp[0] = True
            for num in nums:
                for s in range(k, num - 1, -1):
                    if dp[s - num]:
                        dp[s] = True
            return dp[k]

        n = len(nums)
        res = [False] * n
        for i in range(n):
            cap = capped(i + 1)
            if subSumIsK(cap, k):
                res[i] = True
        return res


class SolutionDpWithSorting:
    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:
        n = len(nums)
        nums.sort()
        ans = [False] * n
        dp = [False] * (k + 1)
        dp[0] = True

        i = 0
        for x in range(1, n + 1):
            # Добавляем все элементы < x (один раз)
            # Потому что все, что < x - остается самим собой для всех последующих итераций
            while i < n and nums[i] < x:
                num = nums[i]
                for j in range(k, num - 1, -1):
                    dp[j] = dp[j] or dp[j - num]
                i += 1

            # Для элементов >= x, считаем сколько раз можно добавить x
            # Они все здесь будут x
            nCapped = n - i
            for j in range(nCapped + 1):
                # Считаем подсумму сумму (все эл. массива одинаковые)
                times = j * x
                if times > k:
                    # Дальше нет смысла искать, потому что подсуммы будут больше суммы
                    break
                if dp[k - times]:
                    # Если нашли вариант, то записываем его
                    ans[x - 1] = True
                    break
        return ans


if __name__ == "__main__":
    nums = [4, 3, 2, 4]
    k = 5

    sol = SolutionDpWithSorting()
    res = sol.subsequenceSumAfterCapping(nums, k)
    print(res)

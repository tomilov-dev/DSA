class Solution:
    def fill_one(self, amount: list[int]):
        time = 0
        amount.sort(reverse=True)
        i = 0
        while amount[i] > 0:
            amount[i] -= 1
            time += 1

        return time

    def fill_both(self, amount: list[int]) -> int:
        time = 0
        amount.sort(reverse=True)
        i = 0
        while amount[i] > 0:
            j = 1 if amount[1] >= amount[2] else 2
            if amount[i] > 0 and amount[j] > 0:
                amount[i] -= 1
                amount[j] -= 1
                time += 1
            else:
                break

        return time

    def fillCups(self, amount: list[int]) -> int:
        time = 0
        time += self.fill_both(amount)
        time += self.fill_both(amount)
        time += self.fill_one(amount)

        return time


if __name__ == "__main__":
    amount = [1, 4, 2]
    amount = [5, 4, 4]

    print(Solution().fillCups(amount))

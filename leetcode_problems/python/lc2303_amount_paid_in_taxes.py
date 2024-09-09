class Solution:
    def calculateTax(
        self,
        brackets: list[list[int]],
        income: int,
    ) -> float:
        cumsum = 0
        incomes = [0 for _ in range(len(brackets))]
        for index in range(len(brackets)):
            inc = brackets[index][0] - cumsum
            inc = min(inc, income)
            incomes[index] = inc
            cumsum += inc

            income -= inc
            income = max(income, 0)

        taxsum = 0
        for index in range(len(brackets)):
            taxsum += incomes[index] * brackets[index][1] / 100

        return taxsum


if __name__ == "__main__":
    brackets = [[3, 50], [7, 10], [12, 25]]
    income = 10

    print(Solution().calculateTax(brackets, income))

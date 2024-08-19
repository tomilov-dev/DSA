class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = [0, 0, 0]  # fives, tens, twenties

        for bill in bills:
            if bill == 5:
                change[0] += 1

            elif bill == 10:
                if change[0] >= 1:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False

            else:
                bill -= 5
                if change[1] >= 1:
                    change[1] -= 1
                    if change[0] >= 1:
                        change[0] -= 1
                        change[2] += 1
                    else:
                        return False
                else:
                    if change[0] >= 3:
                        change[0] -= 3
                        change[2] += 1
                    else:
                        return False

        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]

    print(Solution().lemonadeChange(bills))

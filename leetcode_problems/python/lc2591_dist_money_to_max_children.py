class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        elif children == money:
            return 0

        count, rem = money // 8, money % 8
        while count >= 0:
            if count + rem >= children:
                if children == count + 1 and rem == 4:
                    return count - 1
                if count == children and rem != 0:
                    return count - 1
                elif count > children:
                    count -= 1
                    rem += 8
                else:
                    return count
            else:
                count -= 1
                rem += 8

        return -1


if __name__ == "__main__":
    money = 20
    children = 3

    money = 16
    children = 2

    money = 17
    children = 2

    money = 19
    children = 2

    # money = 12
    # children = 2

    print(Solution().distMoney(money, children))

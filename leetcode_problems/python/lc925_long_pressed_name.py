class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        p2 = 0

        while p2 < len(typed):
            if p1 < len(name) and name[p1] == typed[p2]:
                p1 += 1
            elif p2 == 0 or typed[p2] != typed[p2 - 1]:
                return False
            p2 += 1

        return p1 == len(name)


if __name__ == "__main__":
    name = "alex"
    typed = "aaleex"

    name = "saeed"
    typed = "ssaaedd"

    name = "alex"
    typed = "aaleexa"

    name = "alexd"
    typed = "ale"
    print(Solution().isLongPressedName(name, typed))

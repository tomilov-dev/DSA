class Solution:
    def __init__(self) -> None:
        self.charset = []
        self.charset += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
        self.charset += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.charset += ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.charset += ["_"]
        self.charset = set(self.charset)

        self.lines = set(
            [
                "electronics",
                "grocery",
                "pharmacy",
                "restaurant",
            ]
        )

    def validate_code(self, code: str) -> bool:
        if not code:
            return False

        for c in code:
            if c not in self.charset:
                print(code, "is not valid because of", c)
                return False
        return True

    def validate_line(self, line: str) -> bool:
        if line not in self.lines:
            print(line, "is not valid")
            return False
        return True

    def validate_active(self, active: bool) -> bool:
        return active

    def validateCoupons(
        self,
        code: list[str],
        businessLine: list[str],
        isActive: list[bool],
    ) -> list[str]:
        n = len(code)
        valid = []
        for i in range(n):
            if (
                self.validate_active(isActive[i])
                and self.validate_line(businessLine[i])
                and self.validate_code(code[i])
            ):
                valid.append([businessLine[i], code[i]])

        valid.sort()
        return [v[1] for v in valid]


if __name__ == "__main__":
    code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
    businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
    isActive = [True, True, True, True]
    print(Solution().validateCoupons(code, businessLine, isActive))

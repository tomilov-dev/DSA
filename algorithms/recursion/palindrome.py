class SolutionRecursive:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and self.isPalindrome(s[1:-1])


class SolutionRecursiveTailed:
    def isPalindrome(self, s: str, res: bool = True) -> bool:
        if len(s) <= 1:
            return res
        res &= s[0] == s[-1]
        return self.isPalindrome(s[1:-1], res)


class SolutionIterative:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


class SolutionIterative2:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class SolutionIterativeOneLine:
    def isPalindrome(self, s: str) -> bool:
        return all(s[i] == s[len(s) - i - 1] for i in range(len(s) // 2))


if __name__ == "__main__":
    s = "max"
    print(SolutionRecursive().isPalindrome(s))
    print(SolutionRecursiveTailed().isPalindrome(s))
    print(SolutionIterative().isPalindrome(s))
    print(SolutionIterative2().isPalindrome(s))
    print(SolutionIterativeOneLine().isPalindrome(s))

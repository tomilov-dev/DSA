class SolutionRecursive:
    def removeUtil(self, s: str) -> str:
        sb = ""
        n = len(s)

        i = 0
        while i < n:
            repeated = False
            while i + 1 < n and s[i] == s[i + 1]:
                repeated = True
                i += 1

            if not repeated:
                sb += s[i]
            i += 1

        if n == len(sb):
            return sb
        return self.removeUtil(sb)


if __name__ == "__main__":
    s = "geeksforgeek"
    s = "abccbccba"
    print(SolutionRecursive().removeUtil(s))

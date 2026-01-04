class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return "".join(reversed(s[:k])) + s[k:]


if __name__ == "__main__":
    s = "abcd"
    k = 2
    print(Solution().reversePrefix(s, k))

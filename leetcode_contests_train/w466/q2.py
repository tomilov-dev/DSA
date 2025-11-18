class Solution:
    def minOperations(self, s: str) -> int:
        chars = list(sorted(s))
        n = len(chars)
        total = 0
        index = 0

        # skip 'a'
        while index < n and chars[index] == "a":
            index += 1

        # greedy count
        while index < n:
            char = chars[index]
            while index < n and char == chars[index]:
                index += 1

            if index < n:
                nxt = chars[index]
                add = ord(nxt) - ord(char)
                total += add
            else:
                add = abs(ord("z") - ord(char)) + 1
                total += add

        return total


if __name__ == "__main__":
    s = "yz"
    s = "aaaaxxxyyz"
    s = "a"
    print(Solution().minOperations(s))

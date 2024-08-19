class Solution:
    def minTimeToType(self, word: str) -> int:
        pos = "a"
        types = len(word)

        moves = 0
        for char in word:
            back = (ord(pos) - ord(char)) % 26
            forw = (ord(char) - ord(pos)) % 26

            moves += min(forw, back)
            pos = char

        return types + moves


if __name__ == "__main__":
    # word = "abc"
    # word = "bza"
    word = "zjpc"
    print(Solution().minTimeToType(word))

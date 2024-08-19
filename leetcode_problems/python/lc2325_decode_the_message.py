class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]

        map = dict()

        i = 0
        j = 0
        while i < len(alphabet) and j < len(key):
            if key[j] == " " or key[j] in map:
                j += 1
                continue

            map[key[j]] = alphabet[i]
            i += 1

        msg = []
        for char in message:
            char = char if char not in map else map[char]
            msg.append(char)
        return "".join(msg)


if __name__ == "__main__":
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"

    print(Solution().decodeMessage(key, message))

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        bits = [0, 0]

        for bit in s:
            if bit == "0":
                bits[0] += 1
            else:
                bits[1] += 1

        if bits[1] < 0:
            raise ValueError("Can't create odd number")

        bits[1] -= 1
        odd_num = "1"
        odd_num = "1" * bits[1] + "0" * bits[0] + odd_num
        return odd_num


if __name__ == "__main__":
    s = "0101"
    print(Solution().maximumOddBinaryNumber(s))

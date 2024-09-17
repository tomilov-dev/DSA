class Solution:
    def reverse(self, iter: list):
        p1 = 0
        p2 = len(iter) - 1
        while p1 < p2:
            iter[p1], iter[p2] = iter[p2], iter[p1]
            p1 += 1
            p2 -= 1

    def flipAndInvertImage(
        self,
        image: list[list[int]],
    ) -> list[list[int]]:
        for row in image:
            self.reverse(row)

        for i in range(len(image)):
            for j in range(len(image[j])):
                image[i][j] = image[i][j] ^ 1

        return image


if __name__ == "__main__":
    image = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0],
    ]
    print(Solution().flipAndInvertImage(image))

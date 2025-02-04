class Solution:
    def maxDistToClosest(
        self,
        seats: list[int],
    ) -> int:
        p1 = 0
        p2 = 0
        maxi = 0
        while p1 < len(seats):
            while p2 + 1 < len(seats) and seats[p2] == seats[p2 + 1]:
                p2 += 1

            if seats[p2] == 0:
                if p1 == 0 or p2 == len(seats) - 1:
                    maxi = max(maxi, p2 - p1 + 1)
                else:
                    maxi = max(maxi, (p2 - p1 + 2) // 2)

            p2 += 1
            p1 = p2

        return maxi


if __name__ == "__main__":
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(Solution().maxDistToClosest(seats))

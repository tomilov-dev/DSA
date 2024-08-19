class Solution:
    def minMovesToSeat(
        self,
        seats: list[int],
        students: list[int],
    ) -> int:
        seats.sort()
        students.sort()

        sum = 0
        for i in range(len(seats)):
            sum += abs(seats[i] - students[i])
        return sum


if __name__ == "__main__":
    seats = [3, 1, 5]
    students = [2, 7, 4]

    print(Solution().minMovesToSeat(seats, students))

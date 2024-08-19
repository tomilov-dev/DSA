class Solution:
    def maximumUnits(
        self,
        boxTypes: list[list[int]],
        truckSize: int,
    ) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        units = 0
        index = 0
        while truckSize > 0 and index < len(boxTypes):
            if boxTypes[index][0] <= truckSize:
                units += boxTypes[index][1] * boxTypes[index][0]
                truckSize -= boxTypes[index][0]
            else:
                units += boxTypes[index][1] * truckSize
                truckSize -= truckSize

            index += 1

        return units


if __name__ == "__main__":
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4

    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10

    print(Solution().maximumUnits(boxTypes, truckSize))

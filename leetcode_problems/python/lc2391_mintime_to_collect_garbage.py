class Solution:
    def move_track(
        self,
        tracks: list[int],
        travel: list[int],
        index: int,
        track_index: int,
    ) -> int:
        if tracks[track_index] == index:
            return 0
        else:
            path = sum(travel[tracks[track_index] : index])
            tracks[track_index] = index
            return path

    def garbageCollection(
        self,
        garbage: list[str],
        travel: list[int],
    ) -> int:
        times = 0

        tracks = [0, 0, 0]
        for index in range(len(garbage)):
            garb = garbage[index]
            for char in garb:
                if char == "M":
                    times += self.move_track(tracks, travel, index, 0)
                elif char == "P":
                    times += self.move_track(tracks, travel, index, 1)
                elif char == "G":
                    times += self.move_track(tracks, travel, index, 2)

                times += 1

        return times

    def garbageCollectionOptimized(
        self,
        garbage: list[int],
        travel: list[int],
    ) -> int:
        fib, memo = [0], [0] * 3

        for time in travel:
            fib.append(fib[-1] + time)

        for i in range(len(garbage) - 1, -1, -1):
            v = garbage[i]
            if not memo[0] and "M" in v:
                memo[0] = i
            if not memo[1] and "P" in v:
                memo[1] = i
            if not memo[2] and "G" in v:
                memo[2] = i

            if all(memo):
                break

        return len("".join(garbage)) + (fib[memo[0]] + fib[memo[1]] + fib[memo[2]])


if __name__ == "__main__":
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    print(Solution().garbageCollection(garbage, travel))

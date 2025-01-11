class TimeMap:
    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def is_good(self, cur: int, target: int) -> bool:
        return cur > target

    def get(self, key: str, timestamp: int) -> str:
        records = self.map.get(key, None)
        if records is None:
            return ""

        low = -1
        high = len(records)
        while high - low > 1:
            mid = low + (high - low) // 2
            if self.is_good(records[mid][1], timestamp):
                high = mid
            else:
                low = mid

        return records[low][0] if low >= 0 and low < len(records) else ""


if __name__ == "__main__":
    mapper = TimeMap()
    mapper.set("love", "high", 10)
    mapper.set("love", "low", 20)

    print(mapper.get("love", 5))

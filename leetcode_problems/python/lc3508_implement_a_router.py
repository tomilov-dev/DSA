import bisect
from collections import deque
from collections import defaultdict
from collections import namedtuple


Packet = namedtuple("packet", ["s", "d", "t"])


class Router:
    def __init__(self, memoryLimit: int):
        self._memoryLimit = memoryLimit
        self._packetQueue: deque[Packet] = deque()
        self._uniquePackets: set[Packet] = set()
        self._destTimes: dict[int, list[int]] = defaultdict(list)
        self._destOffset: dict[int, int] = defaultdict(int)

    def _popPacket(self) -> Packet:
        p = self._packetQueue.popleft()
        self._uniquePackets.remove(p)
        self._destOffset[p.d] += 1
        return p

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        p = Packet(source, destination, timestamp)
        if p in self._uniquePackets:
            return False

        if len(self._packetQueue) == self._memoryLimit:
            self._popPacket()

        self._packetQueue.append(p)
        self._uniquePackets.add(p)
        self._destTimes[p.d].append(p.t)
        return True

    def forwardPacket(self) -> list[int]:
        if not self._packetQueue:
            return []
        return list(self._popPacket())

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self._destTimes.get(destination, [])
        offset = self._destOffset.get(destination, 0)
        l = bisect.bisect_left(arr, startTime, offset)
        r = bisect.bisect_right(arr, endTime, offset)
        return r - l

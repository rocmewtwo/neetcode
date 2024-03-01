import heapq
from typing import List


def minMeetingRooms3(intervals: List[int]) -> int:
    # two pointer
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1

        res = max(res, count)

    return res


def minMeetingRooms2(intervals: List[int]) -> int:
    # scan: start + 1, end - 1
    time = []
    for inter in intervals:
        time.append((inter[0], 1))
        time.append((inter[1], -1))

    time.sort(key=lambda x: (x[0], x[1]))

    count = 0
    max_count = 0
    for t in time:
        count += t[1]
        max_count = max(max_count, count)

    return max_count


def minMeetingRooms(intervals: List[int]) -> int:
    # heap
    if not intervals:
        return 0

    intervals.sort()
    # want to quickly find a smallest end of array -> heap
    heap = [intervals[0][1]]  # min heap: end
    for inter in intervals[1:]:
        # release room
        if inter[0] >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, inter[1])

    return len(heap)


# intervals = [(0, 40), (5, 10), (15, 20)]
intervals = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80),
             (80, 90), (90, 100), (0, 100), (10, 90), (20, 80), (30, 70), (40, 60), (50, 50)]


print(minMeetingRooms(intervals))
print(minMeetingRooms2(intervals))
print(minMeetingRooms3(intervals))

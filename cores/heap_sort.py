import heapq


def heap_sort(arr):
    # time: O(nlogn)
    heapq.heapify(arr)
    res = []
    while arr:
        res.append(heapq.heappop(arr))
    return res


arr = [60, 20, 40, 70, 30, 10]
print(heap_sort(arr))

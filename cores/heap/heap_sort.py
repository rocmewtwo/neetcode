import heapq


def heap_sort(arr):
    # time: O(n + nlogn) = O(nlogn)
    heapq.heapify(arr)  # O(n)
    res = []
    while arr:  # n elements
        res.append(heapq.heappop(arr))  # O(logn)
    return res


arr = [60, 20, 40, 70, 30, 10]
print(heap_sort(arr))

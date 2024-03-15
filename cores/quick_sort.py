'''
    base case if end <= start

    pick up right most element as a pivot
    move left pointer to pivot-1
    partition left and right, left < pivot, right > pivot
    swap pivot and left

    recursion 0 - left -1
    recursion left + 1, end
'''


def quick_sort(arr: list[int], s: int, e: int):
    # s: start index, e: end index
    if e <= s:  # base case: single element
        return

    pivot = arr[e]
    left = s  # point left part smaller than pivot

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    # swap end(pivot) and left, move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)


arr = [6, 2, 4, 1, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)

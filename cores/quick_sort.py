import random


def quick_sort(arr, l, r):
    # time O(nlogn), worse case O(n^2)

    if r <= l:
        return

    # random pick pivot and swap to right
    p = random.randrange(l, r)
    arr[r], arr[p] = arr[p], arr[r]

    pivot = arr[r]
    k = l  # swaping position

    # Partition: elements smaller than pivot on left side
    for i in range(l, r):
        if arr[i] < pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1

    # swap pivot
    arr[k], arr[r] = arr[r], arr[k]

    quick_sort(arr, l, k - 1)
    quick_sort(arr, k + 1, r)


arr = [6, 2, 4, 1, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)

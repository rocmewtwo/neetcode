def merge(arr, l, m, r):  # merge in-place
    i = j = 0
    k = l
    arr1 = arr[l: m + 1]  # l to m
    arr2 = arr[m + 1: r + 1]  # m + 1 to r

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1


def merge_sort(arr, l, r):
    if r <= l:
        return arr

    # split
    m = (l + r) // 2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)
    merge(arr, l, m, r)

    return arr


if __name__ == "__main__":
    pairs = [(5, "apple"), (2, "banana"), (9, "cherry"),
             (1, "date"), (9, "elderberry")]

    merge_sort(pairs, 0, len(pairs)-1)
    print(pairs)

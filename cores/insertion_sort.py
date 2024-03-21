from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self) -> str:
        return f"({self.key}, {self.value})"


def insertion_sort(pairs: List[Pair]):
    # time: O(n^2)

    for i in range(len(pairs)):
        j = i - 1
        while (j >= 0 and pairs[j + 1] < pairs[j]):
            pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
            j -= 1


pairs = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]

print(pairs)
insertion_sort(pairs)
print(pairs)

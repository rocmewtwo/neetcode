from typing import List


class MinHeap:
    def __init__(self):
        self.heap = [0]  # ignore first element

    # O(logn)
    def push(self, val: int) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1

        # move up to the proper position
        while index > 1 and self.heap[index // 2] > self.heap[index]:
            # swap
            self.heap[index], self.heap[index //
                                        2] = self.heap[index//2], self.heap[index]
            index = index // 2

    # O(logn)
    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        # move last element to fist
        self.heap[1] = self.heap.pop()
        # bubble down
        self._bubble_down(1)

        return root

    def _bubble_down(self, index) -> None:
        child = 2 * index  # left
        while child < len(self.heap):
            # choose right
            if child+1 < len(self.heap) and self.heap[child+1] < self.heap[child]:
                child += 1

            if self.heap[child] >= self.heap[index]:  # proper position
                break

            # swap
            self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
            index = child
            child = 2 * index

    # O(1)
    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    # O(n)
    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # build from bottom, bubble down every element
        for i in reversed(range(1, len(self.heap) // 2+1)):  # start from last parent
            self._bubble_down(i)

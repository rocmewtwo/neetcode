from typing import List


class MinHeap:
    def __init__(self):
        self.heap = []

    # O(logn)
    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        # move up to the proper position
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # swap
            temp = self.heap[i]
            self.heap[i] = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = temp
            i = self.parent(i)

    # get parent index
    def parent(self, i):
        return (i - 1) // 2

    # get left child index
    def left_child(self, i):
        return (i * 2) + 1

    # get right child index
    def right_child(self, i):
        return (i * 2) + 2

    # remove top element, O(logn)
    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # move last element to fist
        self.heap[0] = self.heap.pop()
        # bubble down
        self._bubble_down(0)

        return root

    def _bubble_down(self, i) -> None:
        child = self.left_child(i)
        curr = i
        while child < len(self.heap):
            # choose right if right < left
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child = child + 1

            if self.heap[child] >= self.heap[curr]:  # proper position
                break

            # swap
            self.heap[curr], self.heap[child] = self.heap[child], self.heap[curr]
            curr = child
            child = self.left_child(curr)

    # O(1)
    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    # O(n)
    def heapify(self, nums: List[int]) -> None:
        self.heap = nums

        # build from bottom, bubble down every element
        # start from last parent, from reversed(0, last+1)
        for i in reversed(range(self.parent(len(self.heap) - 1) + 1)):
            self._bubble_down(i)


if __name__ == "__main__":
    heap = MinHeap()
    heap.heapify([5, 4, 3, 2, 1])
    print(heap.heap)
    print(heap.pop())
    print(heap.top())

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # bool isEmpty() will return whether the queue is empty or not.
    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    # void append(int value) will insert value at the end of the queue.
    def append(self, value: int) -> None:
        node = Node(value)
        prev, next = self.tail.prev, self.tail
        node.prev, node.next = prev, next
        prev.next = node
        next.prev = node

    # void appendleft(int val) will insert value at the beginning of the queue.
    def appendleft(self, value: int) -> None:
        node = Node(value)
        prev, next = self.head, self.head.next
        node.prev, node.next = prev, next
        prev.next = node
        next.prev = node

    # int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
    def pop(self) -> int:
        if self.isEmpty():
            return -1

        node = self.tail.prev
        prev, next = self.tail.prev.prev, self.tail
        prev.next = next
        next.prev = prev
        return node.val

    # int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.
    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head.next
        prev, next = self.head, self.head.next.next
        prev.next = next
        next.prev = prev
        return node.val

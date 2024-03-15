from typing import List


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        # head(dummy node) -> node1 -> node2 (tail) -> None
        self.head = ListNode(-1)  # dummpy node
        self.tail = self.head

    def get(self, index: int) -> int:
        p = self.head.next
        i = 0

        while p:
            if i == index:
                return p.val
            i += 1
            p = p.next

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if self.head == self.tail:  # empty list
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0

        while i < index and prev:
            i += 1
            prev = prev.next

        if prev and prev.next:
            if prev.next == self.tail:  # if remove node is tail, update tail node
                self.tail = prev

            prev.next = prev.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        p = self.head.next
        arr = []

        while p:
            arr.append(p.val)
            p = p.next

        return arr

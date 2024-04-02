# 706. Design HashMap

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.capacity = 100
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if not prev:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                return
            prev, node = node, node.next

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                index = self.hash(node.key)
                new_node = Node(node.key, node.val)
                if not new_table[index]:
                    new_table[index] = new_node
                else:
                    new_node.next = new_table[index]
                    new_table[index] = new_node
                node = node.next
        self.table = new_table

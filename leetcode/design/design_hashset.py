# 705. Design HashSet

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.capacity = 100
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        index = self.hash(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key)
        else:
            prev = None
            while node:
                if node.key == key:
                    return
                prev, node = node, node.next
            prev.next = Node(key)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

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

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                index = self.hash(node.key)
                new_node = Node(node.key)
                if not new_table[index]:
                    new_table[index] = new_node
                else:
                    new_node.next = new_table[index]
                    new_table[index] = new_node
                node = node.next
        self.table = new_table

# Design Hash Table

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        node = self.table[index]

        # insert node
        if not node:  # no collision
            self.table[index] = Node(key, value)
            self.size += 1
        else:  # collision or update value
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev = node
                node = node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._hash(key)

        # search linked list
        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self._hash(key)

        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                # first node
                if not prev:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        # rehashing
        for node in self.table:
            while node:
                index = node.key % self.capacity
                new_node = Node(node.key, node.val)
                if not new_table[index]:
                    new_table[index] = new_node
                else:
                    # collision -> insert to first
                    new_node.next = new_table[index]
                    new_table[index] = new_node
                node = node.next
        self.table = new_table


if __name__ == "__main__":
    hash_table = HashTable(4)
    print(hash_table.insert(1, 2))
    print(hash_table.get(1))
    print(hash_table.insert(1, 3))
    print(hash_table.get(1))
    print(hash_table.remove(1))
    print(hash_table.get(1))

    hash_table = HashTable(2)
    print(hash_table.getCapacity())
    print(hash_table.insert(6, 7))
    print(hash_table.getCapacity())
    print(hash_table.insert(1, 2))
    print(hash_table.getCapacity())
    print(hash_table.insert(3, 4))
    print(hash_table.getCapacity())
    print(hash_table.getSize())

    hash_table = HashTable(4)
    print(hash_table.insert(1, 1))
    print(hash_table.remove(1))
    print(hash_table.insert(2, 2))
    print(hash_table.remove(2))
    print(hash_table.getSize())

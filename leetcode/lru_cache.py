# 146. LRU Cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}  # key: reference to node

        # create doubly linked list
        # left (least use) <-> right (recently use)
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_right(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev = prev.next = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # remove key
        node = self.cache[key]
        self.remove(node)
        self.insert_right(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # cache hit
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert_right(node)
        else:
            # new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert_right(new_node)
            if len(self.cache) > self.size:
                least_node = self.left.next
                self.remove(least_node)
                del self.cache[least_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 133. Clone Graph

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        clone_nodes = {}  # map old to new

        def dfs(node):
            if node in clone_nodes:
                return clone_nodes[node]

            new_node = Node(node.val)
            clone_nodes[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node) if node else None

# Design Graph
from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False

        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        # return self._dfs(src, dst, set())
        return self._bfs(src, dst)

    def _dfs(self, src: int, dst: int, visit: set) -> bool:
        if src == dst:
            return True

        visit.add(src)
        for neighbor in self.adj_list.get(src, set()):
            if neighbor not in visit:
                if self._dfs(neighbor, dst, visit):
                    return True

        return False

    def _bfs(self, src, dst) -> bool:
        queue = deque()
        visit = set()
        queue.append(src)
        visit.add(src)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                for neighbor in self.adj_list.get(node, set()):
                    if neighbor not in visit:
                        queue.append(neighbor)
                        visit.add(neighbor)

        return False

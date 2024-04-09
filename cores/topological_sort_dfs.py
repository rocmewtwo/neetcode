from collections import defaultdict


class Graph:
    def __init__(self, n) -> None:
        self.adj = defaultdict(list)
        self.n = n

    def add_edge(self, n1, n2):
        self.adj[n1].append(n2)

    def topological_sort(self):
        top_sort = []
        visited = set()
        path = set()  # dfs visiting path (used to detect cycle)

        def dfs(node: int) -> bool:
            if node in path:
                return False  # cycle detected

            if node in visited:
                return True

            path.add(node)
            visited.add(node)
            for nei in self.adj[node]:
                if not dfs(nei):
                    return False  # cycle detected

            top_sort.append(node)  # post order: add last
            path.remove(node)  # back

            return True

        for i in range(self.n):
            if not dfs(i):
                return []  # Return an empty list if a cycle is detected

        top_sort.reverse()  # reverse
        return top_sort


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(g.adj)
    print(g.topological_sort())

    g.add_edge(1, 2)  # create cycle
    print(g.adj)
    print(g.topological_sort())

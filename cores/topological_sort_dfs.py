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
        path = set()  # dfs visiting path (used to detch cycle)

        def dfs(node: int) -> bool:
            if node in visited:
                return True
            if node in path:
                return False  # cycle detected

            path.add(node)

            # visit
            for adj_node in self.adj[node]:
                if not dfs(adj_node):
                    return False  # cycle detected

            # post order: add last
            top_sort.append(node)
            visited.add(node)
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

    # g.add_edge(1, 2)  # create cycle
    # print(g.adj)
    # g.topological_sort()

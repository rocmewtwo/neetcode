'''
Kahn's algorithm

Compute the incoming edge of all nodes

Start from 0 incoming edge nodes, put into Queue
(Queue always contains 0 incoming edge node)

While queue is not empty (Traverse nodes in queue)
        dequeue node
        put into topological array
        update the impact nodes to reduce the incoming value (-1)
        if nodes becomes 0 in-degree:
            put into queue

If counter != n:
    has cycle in graph
'''

from collections import deque


class Graph:
    def __init__(self, n) -> None:
        self.adj = {i: [] for i in range(n)}
        self.n = n

    def add_edge(self, n1, n2):
        self.adj[n1].append(n2)

    def topological_sort(self):
        in_degree = [0] * self.n

        # compute in-degree
        for i in self.adj:
            for j in self.adj[i]:
                in_degree[j] += 1

        # queue 0 degree node
        queue = deque()
        for i in range(self.n):
            if in_degree[i] == 0:
                queue.append(i)

        top_sort = []
        # remove 0 degree
        while queue:
            node = queue.popleft()
            top_sort.append(node)

            for adj_node in self.adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)

        if len(top_sort) != self.n:
            print("There exists a cycle in the graph")
        else:
            print(top_sort)


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(g.adj)
    g.topological_sort()

    g.add_edge(1, 2)  # create cycle
    print(g.adj)
    g.topological_sort()

# Union Find (Disjoint set)

class UnionFind:
    def __init__(self, size):
        self.parent = {}
        self.rank = {}

        for i in range(size):
            self.parent[i] = i
            self.rank[i] = 0

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)  # find roots

        # already connected
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

    # Find parent of n, with path compression.
    def find(self, n1: int) -> int:
        p = self.parent[n1]

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # path compression
            p = self.parent[p]
        return p


if __name__ == "__main__":
    size = 4
    uf = UnionFind(size)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)

    print(uf.parent)
    print(uf.rank)

    # Find the root of elements
    for i in range(size):
        print(
            f"Element {i} belongs to the root {uf.find(i)}")

    print(set(uf.find(x) for x in range(size)))

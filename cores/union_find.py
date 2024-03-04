class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def union(self, n1: int, n2: int):
        p1 = self.find(n1)
        p2 = self.find(n2)

        # p1 and p2 have same parent
        if p1 == p2:
            return

        # make the smaller rank as child
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p2] = p1
            self.rank[p2] += self.rank[p1]

    def find(self, n1: int) -> int:
        res = n1

        while res != self.parent[res]:
            # path compression
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res


if __name__ == "__main__":
    size = 4
    uf = UnionFind(size)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)

    print(uf.parent)
    print(uf.rank)

    # Find the representative of each element
    for i in range(size):
        print(
            f"Element {i} belongs to the set with representative {uf.find(i)}")

    print(set(uf.find(x) for x in range(size)))

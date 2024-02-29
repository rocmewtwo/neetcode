class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.end = True

    def print(self):
        def dfs(node, k) -> dict:
            res = {}
            for k, child in node.children.items():
                res[k] = dfs(child, k)
            return res

        res = dfs(self, None)
        print(res)


if __name__ == "__main__":
    trie = TrieNode()

    words = ["oath", "pea", "eat", "rain"]
    for word in words:
        trie.addWord(word)

    trie.print()

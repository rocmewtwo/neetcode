class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startWith(self, prefix) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def print(self):
        def dfs(node, k) -> dict:
            res = {}
            for k, child in node.children.items():
                res[k] = dfs(child, k)
            return res

        res = dfs(self.root, None)
        print(res)


if __name__ == "__main__":
    trie = Trie()

    words = ["oath", "pea", "eat", "rain"]
    for word in words:
        trie.addWord(word)

    trie.print()
    print(trie.search('eat'))
    print(trie.search('ea'))
    print(trie.startWith('ea'))

# No Prefix Set
# https://www.hackerrank.com/challenges/no-prefix-set/problem

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


# time complexity: O(n * m), where n is the number of words and m is the average length of the words
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            if current.word:
                return False
        current.word = True
        return len(current.children) == 0


def noPrefix(words):
    trie = Trie()
    flag = True
    for word in words:
        if not trie.insert(word):
            print('BAD SET', word)
            flag = False
            break
    if flag:
        print('GOOD SET')


# Example 1
words = ['abcd', 'abcde']
noPrefix(words)  # BAD SET a

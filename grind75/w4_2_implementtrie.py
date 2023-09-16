class Trienode:
    def __init__(self):
        self.children = {}
        self.isword = False

class Trie:
    def __init__(self):
        self.root = Trienode()
        
    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Trienode()
            node = node.children[c]
        node.isword = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isword

    def startsWith(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Trie(object):

    def __init__(self):
        self.s = []

    def insert(self, word):
        self.s.append(word)

    def search(self, word):
        return word in self.s

    def startsWith(self, prefix):
        for word in self.s:
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# class Trie(object):

#     def __init__(self):
#         self.s = []

#     def insert(self, word):
#         self.s.append(word)

#     def search(self, word):
#         return word in self.s

#     def startsWith(self, prefix):
#         for word in self.s:
#             if word.startswith(prefix):
#                 return True
#         return False


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)



class Trie(object):

    def __init__(self):
        self.root={}
        

    def insert(self, word):
        node=self.root
        for char in word:
            if char not in node:
                node[char]={}
            node=node[char] 
        node['%'] =True      

        

        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        node=self.root
        for char in word:
            if char not in node:
                return False
            node=node[char]  

        return '%' in node
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        node=self.root
        for char in prefix:
            if char not in node:
                return False
            node=node[char]
        return True

    

        
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
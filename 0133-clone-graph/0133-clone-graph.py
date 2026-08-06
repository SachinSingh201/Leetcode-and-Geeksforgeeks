"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        start = node
        o_to_n = dict()
        stk = [start]
        visited = set()
        visited.add(start)

        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    stk.append(nei)
                    visited.add(nei)
        
        for old,new in o_to_n.items():
            for nei in old.neighbors:
                new_nei = o_to_n[nei]
                new.neighbors.append(new_nei)
        
        return o_to_n[start]

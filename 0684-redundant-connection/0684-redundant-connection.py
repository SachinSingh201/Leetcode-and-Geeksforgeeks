class Solution(object):
    def findRedundantConnection(self, edges):
     

        graph = {}

        for u, v in edges:

            
            visited = set()
            stack = [u]

            while stack:

                node = stack.pop()

                if node == v:
                    return [u, v]

                if node in visited:
                    continue

                visited.add(node)

                for nei in graph.get(node, []):
                    stack.append(nei)

            
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
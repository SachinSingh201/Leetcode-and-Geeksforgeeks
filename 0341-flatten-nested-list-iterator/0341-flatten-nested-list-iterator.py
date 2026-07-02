class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []
        self.flatten(nestedList)
        self.index = 0

    def flatten(self, nested_list):
        """
        Recursively unpacks NestedInteger objects into a flat list.
        """
        for item in nested_list:
            if item.isInteger():
                self.res.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self):
        """
        :rtype: int
        """
        val = self.res[self.index]
        self.index += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.res)

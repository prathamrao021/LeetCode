# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def flatten(self, testlist):
        if isinstance(testlist, list):
            temp = []
            for i in testlist:
                temp += self.flatten(i)
            return temp
        else:
            return [testlist]

    def __init__(self, nestedList):
        self.nested = self.flatten(nestedList)
        self.point = 0

    def next(self) -> int:
        self.point += 1
        if self.point < len(self.nested)-1:
            return self.nested[self.point]
    
    def hasNext(self) -> bool:
        if self.point < len(self.nested)-1:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    n = NestedIterator([[1,1],2,[1,1]])

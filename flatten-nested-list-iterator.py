class NestedIterator:
    def __init__(self, nestedList: 'List[NestedInteger]'):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        return self.stack.pop().getInteger()
        
    def hasNext(self) -> bool:
        while self.stack:
            top_element = self.stack[-1]

            if top_element.isInteger():
                return True
            else:
                self.stack.pop()
                sub_list = top_element.getList()
                for i in range(len(sub_list) - 1, -1, -1):
                    self.stack.append(sub_list[i])
        
        return False

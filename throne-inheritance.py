class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children[childName] = []
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        order = []
        stack = [self.king]
        while stack:
            cur = stack.pop()
            if cur not in self.dead:
                order.append(cur)
            for child in reversed(self.children.get(cur, [])):
                stack.append(child)
        return order

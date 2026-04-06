class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()

        def recover(node: TreeNode, current_val: int):
            if not node:
                return

            self.values.add(current_val)

            if node.left:
                recover(node.left, 2 * current_val + 1)
            if node.right:
                recover(node.right, 2 * current_val + 2)

        recover(root, 0)


    def find(self, target: int) -> bool:
        return target in self.values
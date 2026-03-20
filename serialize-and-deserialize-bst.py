# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        nodes = []
        def preorder(node):
            if not node:
                return
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(nodes)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        self.nodes_list = [int(x) for x in data.split(',')]
        self.idx = 0

        def _deserialize_helper(min_val, max_val):
            if self.idx >= len(self.nodes_list):
                return None

            val = self.nodes_list[self.idx]

            if not (min_val < val < max_val):
                return None

            root = TreeNode(val)
            self.idx += 1

            root.left = _deserialize_helper(min_val, val)
            root.right = _deserialize_helper(val, max_val)

            return root

        return _deserialize_helper(float('-inf'), float('inf'))

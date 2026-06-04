# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        import sys
        sys.setrecursionlimit(300000)
        node_map = {}
        def dfs1(node, depth):
            node_map[node.val] = node
            node.depth = depth
            left = dfs1(node.left, depth + 1) if node.left else -1
            right = dfs1(node.right, depth + 1) if node.right else -1
            node.subtree_max = max(left, right, depth)
            return node.subtree_max
        dfs1(root, 0)
        def dfs2(node, up_max):
            node.up_max = up_max
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            top1 = top2 = -1
            for child in children:
                val = child.subtree_max
                if val > top1:
                    top2 = top1
                    top1 = val
                elif val > top2:
                    top2 = val
            for child in children:
                sibling_max = top1 if child.subtree_max != top1 else top2
                child_up = max(up_max, sibling_max, node.depth)
                dfs2(child, child_up)
        dfs2(root, -1)
        return [node_map[q].up_max for q in queries]

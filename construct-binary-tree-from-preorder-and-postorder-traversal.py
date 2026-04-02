
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        val_to_post_idx = {val: i for i, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start == pre_end:
                return None

            root_val = preorder[pre_start]
            node = TreeNode(root_val)
            if pre_end - pre_start == 1:
                return node

            left_subtree_root_val = preorder[pre_start + 1]
            idx_in_original_postorder = val_to_post_idx[left_subtree_root_val]
            
            num_left_nodes = idx_in_original_postorder - post_start + 1

            node.left = build(
                pre_start + 1,
                pre_start + 1 + num_left_nodes,
                post_start,
                post_start + num_left_nodes
            )

            node.right = build(
                pre_start + 1 + num_left_nodes,
                pre_end,
                post_start + num_left_nodes,
                post_end - 1
            )

            return node

        return build(0, len(preorder), 0, len(postorder))

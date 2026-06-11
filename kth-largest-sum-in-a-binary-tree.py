# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque
        import heapq
        if not root:
            return -1
        queue = deque([root])
        sums = []
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(level_sum)
        if len(sums) < k:
            return -1
        kth = heapq.nlargest(k, sums)[-1]
        return kth

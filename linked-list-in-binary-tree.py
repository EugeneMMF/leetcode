class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(node, current_list_node):
            if not node:
                return False
            
            if node.val == current_list_node.val:
                if not current_list_node.next:
                    return True
                return dfs(node.left, current_list_node.next) or dfs(node.right, current_list_node.next)
            else:
                return False

        def check(node, list_head):
            if not node:
                return False
            
            if dfs(node, list_head):
                return True
            
            return check(node.left, list_head) or check(node.right, list_head)
        
        return check(root, head)


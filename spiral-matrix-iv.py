# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        node = head
        while node and top <= bottom and left <= right:
            for col in range(left, right + 1):
                if not node:
                    break
                matrix[top][col] = node.val
                node = node.next
            top += 1
            for row in range(top, bottom + 1):
                if not node:
                    break
                matrix[row][right] = node.val
                node = node.next
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if not node:
                        break
                    matrix[bottom][col] = node.val
                    node = node.next
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if not node:
                        break
                    matrix[row][left] = node.val
                    node = node.next
                left += 1
        return matrix

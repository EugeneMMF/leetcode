class Solution:
    def __init__(self):
        self.memo = {}

    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        if n in self.memo:
            return self.memo[n]

        result = []
        for i in range(1, n, 2):
            j = n - 1 - i
            
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(j)

            for left_root in left_subtrees:
                for right_root in right_subtrees:
                    root = TreeNode(0, left_root, right_root)
                    result.append(root)
        
        self.memo[n] = result
        return result

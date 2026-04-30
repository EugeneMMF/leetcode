class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        indexed_queries = [(mi, xi, i) for i, (xi, mi) in enumerate(queries)]
        indexed_queries.sort()
        class Node:
            __slots__ = ('child',)
            def __init__(self):
                self.child = [None, None]
        root = Node()
        def insert(val):
            node = root
            for k in range(30, -1, -1):
                b = (val >> k) & 1
                if not node.child[b]:
                    node.child[b] = Node()
                node = node.child[b]
        def query(val):
            node = root
            if not node.child[0] and not node.child[1]:
                return -1
            res = 0
            for k in range(30, -1, -1):
                b = (val >> k) & 1
                want = 1 - b
                if node.child[want]:
                    res |= (1 << k)
                    node = node.child[want]
                else:
                    node = node.child[b]
            return res
        ans = [0] * len(queries)
        idx = 0
        n = len(nums)
        for mi, xi, i in indexed_queries:
            while idx < n and nums[idx] <= mi:
                insert(nums[idx])
                idx += 1
            ans[i] = query(xi)
        return ans

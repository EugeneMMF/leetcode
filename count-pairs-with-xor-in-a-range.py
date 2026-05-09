class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        maxbit = 15
        def count_with_limit(limit: int) -> int:
            if limit < 0:
                return 0
            nodes = [{'cnt': 0, 0: None, 1: None}]
            def insert(num: int):
                node = nodes[0]
                for i in range(maxbit - 1, -1, -1):
                    bit = (num >> i) & 1
                    if node[bit] is None:
                        node[bit] = {'cnt': 0, 0: None, 1: None}
                        nodes.append(node[bit])
                    node = node[bit]
                    node['cnt'] += 1
            def query(num: int) -> int:
                node = nodes[0]
                res = 0
                for i in range(maxbit - 1, -1, -1):
                    if node is None:
                        break
                    num_bit = (num >> i) & 1
                    limit_bit = (limit >> i) & 1
                    if limit_bit == 1:
                        child_same = node.get(num_bit)
                        if child_same:
                            res += child_same['cnt']
                        node = node.get(1 - num_bit)
                    else:
                        node = node.get(num_bit)
                if node:
                    res += node['cnt']
                return res
            total = 0
            for num in nums:
                total += query(num)
                insert(num)
            return total
        return count_with_limit(high) - count_with_limit(low - 1)

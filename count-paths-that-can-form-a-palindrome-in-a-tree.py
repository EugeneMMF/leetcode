class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        freq = {}
        ans = 0
        stack = [(0, 0)]
        while stack:
            node, mask = stack.pop()
            cnt = freq.get(mask, 0)
            ans += cnt
            for b in range(26):
                ans += freq.get(mask ^ (1 << b), 0)
            freq[mask] = cnt + 1
            for child in children[node]:
                bit = 1 << (ord(s[child]) - 97)
                stack.append((child, mask ^ bit))
        return ans

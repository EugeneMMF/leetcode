class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        masks = []
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            masks.append(m)
        mask_to_indices = {}
        for i, m in enumerate(masks):
            mask_to_indices.setdefault(m, []).append(i)
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        for indices in mask_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])
        unique_masks = list(mask_to_indices.keys())
        mask_set = set(unique_masks)
        for m in unique_masks:
            idx = mask_to_indices[m][0]
            present = [i for i in range(26) if (m >> i) & 1]
            absent = [i for i in range(26) if not ((m >> i) & 1)]
            for i in present:
                m_del = m & ~(1 << i)
                if m_del in mask_set:
                    union(idx, mask_to_indices[m_del][0])
                for j in absent:
                    m_rep = m_del | (1 << j)
                    if m_rep in mask_set:
                        union(idx, mask_to_indices[m_rep][0])
            for j in absent:
                m_add = m | (1 << j)
                if m_add in mask_set:
                    union(idx, mask_to_indices[m_add][0])
        comp_size = {}
        for i in range(n):
            r = find(i)
            comp_size[r] = comp_size.get(r, 0) + 1
        max_groups = len(comp_size)
        largest = max(comp_size.values())
        return [max_groups, largest]

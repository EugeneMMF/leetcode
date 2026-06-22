class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        count = 0
        ans = []
        for idx, col in queries:
            if colors[idx] == col:
                ans.append(count)
                continue
            old = colors[idx]
            if old != 0:
                if idx > 0 and colors[idx - 1] == old:
                    count -= 1
                if idx < n - 1 and colors[idx + 1] == old:
                    count -= 1
            colors[idx] = col
            if col != 0:
                if idx > 0 and colors[idx - 1] == col:
                    count += 1
                if idx < n - 1 and colors[idx + 1] == col:
                    count += 1
            ans.append(count)
        return ans

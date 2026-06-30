class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]
        h_set = set()
        for i in range(len(h)):
            for j in range(i):
                h_set.add(h[i] - h[j])
        v_set = set()
        for i in range(len(v)):
            for j in range(i):
                v_set.add(v[i] - v[j])
        common = h_set & v_set
        if not common:
            return -1
        max_side = max(common)
        return (max_side * max_side) % MOD

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        m = len(artifacts)
        total_cells = [0] * m
        uncovered = [0] * m
        cell_to_art = {}
        for idx, (r1, c1, r2, c2) in enumerate(artifacts):
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    total_cells[idx] += 1
                    cell_to_art[(r, c)] = idx
        for r, c in dig:
            if (r, c) in cell_to_art:
                art_id = cell_to_art[(r, c)]
                uncovered[art_id] += 1
        return sum(1 for i in range(m) if uncovered[i] == total_cells[i])

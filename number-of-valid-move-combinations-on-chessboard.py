class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dirs = {
            "rook": [(1,0),(-1,0),(0,1),(0,-1)],
            "bishop": [(1,1),(1,-1),(-1,1),(-1,-1)],
            "queen": [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        }
        n = len(pieces)
        starts = [(r-1,c-1) for r,c in positions]
        all_paths = []
        for typ,(sr,sc) in zip(pieces,starts):
            dests = []
            dests.append((sr,sc))
            for dr,dc in dirs[typ]:
                nr, nc = sr+dr, sc+dc
                while 0 <= nr < 8 and 0 <= nc < 8:
                    dests.append((nr,nc))
                    nr += dr
                    nc += dc
            paths = []
            for tr,tc in dests:
                steps = max(abs(tr-sr), abs(tc-sc))
                if steps == 0:
                    path = [(sr,sc)]
                else:
                    step_r = (tr-sr)//steps
                    step_c = (tc-sc)//steps
                    path = [(sr + k*step_r, sc + k*step_c) for k in range(steps+1)]
                paths.append(path)
            all_paths.append(paths)
        count = 0
        chosen = []
        def dfs(idx):
            nonlocal count
            if idx == n:
                count += 1
                return
            for path in all_paths[idx]:
                ok = True
                for prev_path in chosen:
                    maxlen = max(len(path), len(prev_path))
                    for t in range(maxlen):
                        pa = path[t] if t < len(path) else path[-1]
                        pb = prev_path[t] if t < len(prev_path) else prev_path[-1]
                        if pa == pb:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    chosen.append(path)
                    dfs(idx+1)
                    chosen.pop()
        dfs(0)
        return count

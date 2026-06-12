class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        target = (m - 1, n - 1)
        if (0, 0) == target:
            return 1
        # Prepare sorted lists of remaining columns per row and rows per column
        rows = [list(range(n)) for _ in range(m)]
        cols = [list(range(m)) for _ in range(n)]
        # Helper to remove a value from a sorted list
        def remove_from_sorted(lst, val):
            import bisect
            idx = bisect.bisect_left(lst, val)
            if idx < len(lst) and lst[idx] == val:
                lst.pop(idx)
        # Mark start visited
        remove_from_sorted(rows[0], 0)
        remove_from_sorted(cols[0], 0)
        q = deque()
        q.append((0, 0, 1))
        import bisect
        while q:
            i, j, steps = q.popleft()
            max_jump = grid[i][j]
            # Rightward moves
            if max_jump > 0:
                row_list = rows[i]
                left = bisect.bisect_right(row_list, j)
                right = bisect.bisect_right(row_list, j + max_jump)
                to_visit = row_list[left:right]
                # Remove them from row_list and cols
                for col in to_visit:
                    q.append((i, col, steps + 1))
                    remove_from_sorted(cols[col], i)
                del row_list[left:right]
            # Downward moves
            if max_jump > 0:
                col_list = cols[j]
                left = bisect.bisect_right(col_list, i)
                right = bisect.bisect_right(col_list, i + max_jump)
                to_visit = col_list[left:right]
                for row in to_visit:
                    q.append((row, j, steps + 1))
                    remove_from_sorted(rows[row], j)
                del col_list[left:right]
            # Check if target reached in queue processing
            if q and q[0][0] == target[0] and q[0][1] == target[1]:
                return q[0][2]
        return -1

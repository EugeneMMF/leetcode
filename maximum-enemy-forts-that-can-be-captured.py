class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last_index = -1
        last_type = 0
        max_capture = 0
        for i, val in enumerate(forts):
            if val == 0:
                continue
            if last_type and last_type != val:
                captured = i - last_index - 1
                if captured > max_capture:
                    max_capture = captured
            last_index = i
            last_type = val
        return max_capture

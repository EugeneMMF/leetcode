class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zero_pos = [i for i, ch in enumerate(s) if ch == '0']
        total = 0
        # substrings with no zeros
        run = 0
        for ch in s:
            if ch == '1':
                run += 1
            else:
                total += run * (run + 1) // 2
                run = 0
        total += run * (run + 1) // 2
        # substrings with z zeros, z >= 1
        max_z = int(n ** 0.5) + 2
        zcnt = len(zero_pos)
        for z in range(1, max_z + 1):
            if zcnt < z:
                break
            need_len = z * z + z
            if need_len > n:
                continue
            for i in range(zcnt - z + 1):
                prev_zero = zero_pos[i - 1] if i > 0 else -1
                next_zero = zero_pos[i + z] if i + z < zcnt else n
                start_low = prev_zero + 1
                start_high = zero_pos[i]
                end_low = zero_pos[i + z - 1]
                end_high = next_zero - 1
                for start in range(start_low, start_high + 1):
                    min_end = max(end_low, start + need_len - 1)
                    if min_end <= end_high:
                        total += end_high - min_end + 1
        return total
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        pow3 = [1]
        for _ in range(n):
            pow3.append(pow3[-1] * 3)
        total_masks = pow3[n]
        base = [0, 120, 40]
        delta = [0, -30, 20]
        intro_cnt = [0] * total_masks
        extro_cnt = [0] * total_masks
        internal = [0] * total_masks
        for mask in range(total_masks):
            cnt_i = cnt_e = 0
            happ = 0
            prev_type = 0
            for c in range(n):
                t = (mask // pow3[c]) % 3
                if t == 1:
                    cnt_i += 1
                elif t == 2:
                    cnt_e += 1
                if t:
                    happ += base[t]
                    if c and prev_type:
                        happ += delta[t] + delta[prev_type]
                prev_type = t
            intro_cnt[mask] = cnt_i
            extro_cnt[mask] = cnt_e
            internal[mask] = happ
        vertical = [[0] * total_masks for _ in range(total_masks)]
        for pm in range(total_masks):
            for cm in range(total_masks):
                add = 0
                for c in range(n):
                    t_up = (pm // pow3[c]) % 3
                    t_cur = (cm // pow3[c]) % 3
                    if t_up and t_cur:
                        add += delta[t_up] + delta[t_cur]
                vertical[pm][cm] = add
        from collections import defaultdict
        dp = defaultdict(lambda: -10**9)
        dp[(0, introvertsCount, extrovertsCount)] = 0
        for _ in range(m):
            ndp = defaultdict(lambda: -10**9)
            for (prev_mask, i_left, e_left), val in dp.items():
                for cur_mask in range(total_masks):
                    ic = intro_cnt[cur_mask]
                    ec = extro_cnt[cur_mask]
                    if ic <= i_left and ec <= e_left:
                        ni = i_left - ic
                        ne = e_left - ec
                        nv = val + internal[cur_mask] + vertical[prev_mask][cur_mask]
                        key = (cur_mask, ni, ne)
                        if nv > ndp[key]:
                            ndp[key] = nv
            dp = ndp
        ans = 0
        for v in dp.values():
            if v > ans:
                ans = v
        return ans

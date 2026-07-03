class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        max_u = max_v = -10**18
        min_u = min_v = 10**18
        cnt_max_u = cnt_min_u = cnt_max_v = cnt_min_v = 0
        second_max_u = second_max_v = -10**18
        second_min_u = second_min_v = 10**18
        us = []
        vs = []
        for x, y in points:
            u = x + y
            v = x - y
            us.append(u)
            vs.append(v)
            if u > max_u:
                second_max_u = max_u
                max_u = u
                cnt_max_u = 1
            elif u == max_u:
                cnt_max_u += 1
            elif u > second_max_u:
                second_max_u = u
            if u < min_u:
                second_min_u = min_u
                min_u = u
                cnt_min_u = 1
            elif u == min_u:
                cnt_min_u += 1
            elif u < second_min_u:
                second_min_u = u
            if v > max_v:
                second_max_v = max_v
                max_v = v
                cnt_max_v = 1
            elif v == max_v:
                cnt_max_v += 1
            elif v > second_max_v:
                second_max_v = v
            if v < min_v:
                second_min_v = min_v
                min_v = v
                cnt_min_v = 1
            elif v == min_v:
                cnt_min_v += 1
            elif v < second_min_v:
                second_min_v = v
        best = 10**18
        for u, v in zip(us, vs):
            new_max_u = max_u if not (u == max_u and cnt_max_u == 1) else second_max_u
            new_min_u = min_u if not (u == min_u and cnt_min_u == 1) else second_min_u
            diff_u = new_max_u - new_min_u
            new_max_v = max_v if not (v == max_v and cnt_max_v == 1) else second_max_v
            new_min_v = min_v if not (v == min_v and cnt_min_v == 1) else second_min_v
            diff_v = new_max_v - new_min_v
            best = min(best, max(diff_u, diff_v))
        return best

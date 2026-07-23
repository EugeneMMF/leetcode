from typing import List
import bisect

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        end0 = [0]*n
        end1 = [0]*n
        endBoth = [0]*n
        r = 0
        z = 0
        for l in range(n):
            while r < n and z + (s[r] == '0') <= k:
                if s[r] == '0':
                    z += 1
                r += 1
            end0[l] = r-1
            if s[l] == '0':
                z -= 1
        r = 0
        o = 0
        for l in range(n):
            while r < n and o + (s[r] == '1') <= k:
                if s[r] == '1':
                    o += 1
                r += 1
            end1[l] = r-1
            if s[l] == '1':
                o -= 1
        r = 0
        z = 0
        o = 0
        for l in range(n):
            while r < n and z + (s[r] == '0') <= k and o + (s[r] == '1') <= k:
                if s[r] == '0':
                    z += 1
                else:
                    o += 1
                r += 1
            endBoth[l] = r-1
            if s[l] == '0':
                z -= 1
            else:
                o -= 1
        arr0 = [0]*n
        arr1 = [0]*n
        arrB = [0]*n
        for i in range(n):
            v0 = end0[i]-i+1
            v1 = end1[i]-i+1
            vB = endBoth[i]-i+1
            arr0[i] = v0 if v0 > 0 else 0
            arr1[i] = v1 if v1 > 0 else 0
            arrB[i] = vB if vB > 0 else 0
        pref0 = [0]*n
        pref1 = [0]*n
        prefB = [0]*n
        prefI = [0]*n
        for i in range(n):
            pref0[i] = arr0[i] + (pref0[i-1] if i else 0)
            pref1[i] = arr1[i] + (pref1[i-1] if i else 0)
            prefB[i] = arrB[i] + (prefB[i-1] if i else 0)
            prefI[i] = i + (prefI[i-1] if i else 0)
        def range_sum(pref, l, r):
            if l > r:
                return 0
            return pref[r] - (pref[l-1] if l else 0)
        def count_for(end, prefEnd, l, r):
            if l > r:
                return 0
            idx = bisect.bisect_left(end, r+1)
            if idx < l:
                idx = l
            if idx > r:
                return range_sum(prefEnd, l, r)
            sum1 = range_sum(prefEnd, l, idx-1)
            cnt = r - idx + 1
            sum_i = range_sum(prefI, idx, r)
            sum2 = cnt * (r+1) - sum_i
            return sum1 + sum2
        ans = []
        for l, r in queries:
            c0 = count_for(end0, pref0, l, r)
            c1 = count_for(end1, pref1, l, r)
            cB = count_for(endBoth, prefB, l, r)
            ans.append(c0 + c1 - cB)
        return ans
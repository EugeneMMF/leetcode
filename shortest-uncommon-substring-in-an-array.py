class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        res = []
        for i in range(n):
            found = ""
            s = arr[i]
            L = len(s)
            for l in range(1, L + 1):
                subs = set()
                for start in range(0, L - l + 1):
                    subs.add(s[start:start + l])
                for sub in sorted(subs):
                    ok = True
                    for j in range(n):
                        if j == i:
                            continue
                        if sub in arr[j]:
                            ok = False
                            break
                    if ok:
                        found = sub
                        break
                if found:
                    break
            res.append(found)
        return res

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        cnt = 0
        for x in arr1:
            ok = True
            for y in arr2:
                if abs(x - y) <= d:
                    ok = False
                    break
            if ok:
                cnt += 1
        return cnt

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + original[i] - original[i - 1]
        maxL = -10**20
        minR = 10**20
        for i in range(n):
            l = bounds[i][0] - pref[i]
            r = bounds[i][1] - pref[i]
            if l > maxL:
                maxL = l
            if r < minR:
                minR = r
        if maxL > minR:
            return 0
        return minR - maxL + 1
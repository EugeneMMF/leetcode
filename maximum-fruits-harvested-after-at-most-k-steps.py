class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        from bisect import bisect_left, bisect_right
        n = len(fruits)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + fruits[i][1]
        positions = [p for p, _ in fruits]
        left = bisect_left(positions, startPos - k)
        right = bisect_right(positions, startPos + k) - 1
        if left > right:
            return 0
        ans = 0
        for i in range(left, right + 1):
            left_pos = fruits[i][0]
            steps_left = startPos - left_pos
            if steps_left > k:
                continue
            remaining = k - 2 * steps_left
            max_right_pos = startPos + remaining
            j = bisect_right(positions, max_right_pos, i, right + 1) - 1
            total = pref[j + 1] - pref[i]
            if total > ans:
                ans = total
        for i in range(left, right + 1):
            right_pos = fruits[i][0]
            steps_right = right_pos - startPos
            if steps_right > k:
                continue
            remaining = k - 2 * steps_right
            min_left_pos = startPos - remaining
            j = bisect_left(positions, min_left_pos, left, i + 1)
            total = pref[i + 1] - pref[j]
            if total > ans:
                ans = total
        return ans
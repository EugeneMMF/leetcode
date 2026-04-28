class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count('a')
        prefix_b = 0
        suffix_a = total_a
        ans = min(total_a, len(s) - total_a)
        for ch in s:
            if ch == 'b':
                prefix_b += 1
            else:
                suffix_a -= 1
            deletions = prefix_b + suffix_a
            if deletions < ans:
                ans = deletions
        return ans

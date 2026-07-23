class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n * (n + 1) // 2
        counts = [0] * 26
        ans = 0
        right = 0
        flag = False
        for left in range(n):
            if right < left:
                right = left
                counts = [0] * 26
                flag = False
            while right < n and not flag:
                idx = ord(s[right]) - 97
                counts[idx] += 1
                if counts[idx] >= k:
                    flag = True
                right += 1
            if flag:
                ans += n - right + 1
            idx = ord(s[left]) - 97
            counts[idx] -= 1
            if counts[idx] == k - 1:
                flag = any(c >= k for c in counts)
        return ans

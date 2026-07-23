class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = {}
        for w in words:
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
        n = len(target)
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            node = root
            for j in range(i, n):
                ch = target[j]
                if ch not in node:
                    break
                node = node[ch]
                if dp[j + 1] > dp[i] + 1:
                    dp[j + 1] = dp[i] + 1
        return dp[n] if dp[n] != INF else -1
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int) -> bool:
            memo = {}
            def dfs(pos: int, rem: int) -> bool:
                if pos == len(s):
                    return rem == 0
                key = (pos, rem)
                if key in memo:
                    return memo[key]
                for end in range(pos + 1, len(s) + 1):
                    val = int(s[pos:end])
                    if val > rem:
                        continue
                    if dfs(end, rem - val):
                        memo[key] = True
                        return True
                memo[key] = False
                return False
            return dfs(0, target)
        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                total += sq
        return total

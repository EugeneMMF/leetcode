class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        block = n // k
        s_blocks = [s[i*block:(i+1)*block] for i in range(k)]
        t_blocks = [t[i*block:(i+1)*block] for i in range(k)]
        return sorted(s_blocks) == sorted(t_blocks)
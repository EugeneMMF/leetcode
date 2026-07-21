class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k_mod = k % n
        return ''.join(s[(i + k_mod) % n] for i in range(n))

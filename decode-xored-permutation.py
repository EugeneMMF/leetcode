class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]
        perm = [total ^ odd_xor]
        for v in encoded:
            perm.append(perm[-1] ^ v)
        return perm

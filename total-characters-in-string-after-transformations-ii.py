class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        size = 26
        M = [[0]*size for _ in range(size)]
        for i in range(size):
            for k in range(1, nums[i]+1):
                M[i][(i+k)%size] = 1
        def mat_mult(A, B):
            C = [[0]*size for _ in range(size)]
            for i in range(size):
                Ai = A[i]
                Ci = C[i]
                for k in range(size):
                    aik = Ai[k]
                    if aik:
                        Bk = B[k]
                        for j in range(size):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % mod
            return C
        def mat_pow(mat, exp):
            res = [[0]*size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            base = mat
            while exp:
                if exp & 1:
                    res = mat_mult(res, base)
                base = mat_mult(base, base)
                exp >>= 1
            return res
        Mt = mat_pow(M, t)
        v0 = [0]*size
        for ch in s:
            v0[ord(ch)-97] += 1
        vt = [0]*size
        for i in range(size):
            vi = v0[i]
            if vi:
                row = Mt[i]
                for j in range(size):
                    vt[j] = (vt[j] + vi * row[j]) % mod
        return sum(vt) % mod
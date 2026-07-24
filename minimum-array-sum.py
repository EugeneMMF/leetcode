class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        INF = 10**18
        dp_cur = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
        dp_cur[0][0] = 0
        for val in nums:
            dp_next = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
            ceil_half = (val + 1) // 2
            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    cur = dp_cur[a][b]
                    if cur == INF:
                        continue
                    # none
                    if dp_next[a][b] > cur + val:
                        dp_next[a][b] = cur + val
                    # op1 only
                    if a + 1 <= op1:
                        v1 = ceil_half
                        if dp_next[a + 1][b] > cur + v1:
                            dp_next[a + 1][b] = cur + v1
                    # op2 only
                    if b + 1 <= op2 and val >= k:
                        v2 = val - k
                        if dp_next[a][b + 1] > cur + v2:
                            dp_next[a][b + 1] = cur + v2
                    # both
                    if a + 1 <= op1 and b + 1 <= op2:
                        # op1 then op2
                        v_a = ceil_half
                        if v_a >= k:
                            v_a -= k
                        # op2 then op1
                        v_b = val
                        if val >= k:
                            v_b -= k
                        v_b = (v_b + 1) // 2
                        v_both = v_a if v_a < v_b else v_b
                        if dp_next[a + 1][b + 1] > cur + v_both:
                            dp_next[a + 1][b + 1] = cur + v_both
            dp_cur = dp_next
        ans = INF
        for a in range(op1 + 1):
            for b in range(op2 + 1):
                if dp_cur[a][b] < ans:
                    ans = dp_cur[a][b]
        return ans

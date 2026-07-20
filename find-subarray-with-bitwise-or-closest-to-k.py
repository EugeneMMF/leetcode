from typing import List
import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = int(math.log2(n)) + 1
        st = [[0]*logn for _ in range(n)]
        for i in range(n):
            st[i][0] = nums[i]
        j = 1
        while (1 << j) <= n:
            for i in range(n - (1 << j) + 1):
                st[i][j] = st[i][j-1] | st[i + (1 << (j-1))][j-1]
            j += 1
        logs = [0]*(n+1)
        for i in range(2, n+1):
            logs[i] = logs[i//2] + 1
        def query(l, r):
            length = r - l + 1
            j = logs[length]
            return st[l][j] | st[r - (1 << j) + 1][j]
        ans = abs(k - nums[0])
        for l in range(n):
            low, high = l, n-1
            res = -1
            while low <= high:
                mid = (low + high)//2
                if query(l, mid) >= k:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if res != -1:
                val = query(l, res)
                ans = min(ans, abs(val - k))
                if res > l:
                    val2 = query(l, res-1)
                    ans = min(ans, abs(val2 - k))
            else:
                val = query(l, n-1)
                ans = min(ans, abs(val - k))
        return ans

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        cnt = 0
        idx = len(fib) - 1
        while k > 0:
            while fib[idx] > k:
                idx -= 1
            k -= fib[idx]
            cnt += 1
        return cnt

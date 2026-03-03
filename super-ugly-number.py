class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly_numbers = [1]
        
        pointers = [0] * len(primes)
        
        for _ in range(1, n):
            min_next_ugly = float('inf')
            
            for i in range(len(primes)):
                candidate = primes[i] * ugly_numbers[pointers[i]]
                min_next_ugly = min(min_next_ugly, candidate)
            
            ugly_numbers.append(min_next_ugly)
            
            for i in range(len(primes)):
                if primes[i] * ugly_numbers[pointers[i]] == min_next_ugly:
                    pointers[i] += 1
                    
        return ugly_numbers[n - 1]

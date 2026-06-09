class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes=set()
        for n in nums:
            x=n
            d=2
            while d*d<=x:
                if x%d==0:
                    primes.add(d)
                    while x%d==0:
                        x//=d
                d+=1 if d==2 else 2
            if x>1:
                primes.add(x)
        return len(primes)

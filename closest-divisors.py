class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        def find_closest_divisors_for_target(n):
            a, b = 1, n
            i = 1
            while i * i <= n:
                if n % i == 0:
                    a = i
                    b = n // i
                i += 1
            return a, b

        target1 = num + 1
        target2 = num + 2

        a1, b1 = find_closest_divisors_for_target(target1)
        a2, b2 = find_closest_divisors_for_target(target2)

        if abs(a1 - b1) <= abs(a2 - b2):
            return [a1, b1]
        else:
            return [a2, b2]

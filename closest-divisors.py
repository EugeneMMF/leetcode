class Solution:
    def closestDivisors(self, num: int):
        import math
        best_pair = None
        best_diff = None
        for add in (1, 2):
            target = num + add
            root = int(math.isqrt(target))
            for i in range(root, 0, -1):
                if target % i == 0:
                    a, b = i, target // i
                    diff = b - a
                    if best_diff is None or diff < best_diff:
                        best_diff = diff
                        best_pair = [a, b]
                    break
        return best_pair

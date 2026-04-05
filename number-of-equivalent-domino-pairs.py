class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = [0] * 100
        
        for domino in dominoes:
            a, b = domino[0], domino[1]
            
            if a > b:
                a, b = b, a
            
            key = a * 10 + b
            counts[key] += 1
        
        total_pairs = 0
        for count in counts:
            total_pairs += (count * (count - 1)) // 2
        
        return total_pairs


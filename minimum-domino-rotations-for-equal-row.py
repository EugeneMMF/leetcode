class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target: int) -> int:
            rotations_top = 0
            rotations_bottom = 0
            
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                
                if tops[i] != target:
                    rotations_top += 1
                
                if bottoms[i] != target:
                    rotations_bottom += 1
            
            return min(rotations_top, rotations_bottom)

        rotations1 = check(tops[0])
        rotations2 = check(bottoms[0])

        ans = min(rotations1, rotations2)
        
        if ans == float('inf'):
            return -1
        else:
            return ans

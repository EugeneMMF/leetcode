class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_xy = 0
        count_yx = 0

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x' and s2[i] == 'y':
                count_xy += 1
            else:
                count_yx += 1
        
        if (count_xy + count_yx) % 2 != 0:
            return -1
        
        swaps = 0
        
        swaps += count_xy // 2
        swaps += count_yx // 2
        
        if count_xy % 2 == 1:
            swaps += 2
            
        return swaps

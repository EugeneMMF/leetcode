class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        sum_all_nums = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if sum_all_nums < desiredTotal:
            return False

        memo = {}

        def can_win(mask: int, remaining_total: int) -> bool:
            if (mask, remaining_total) in memo:
                return memo[(mask, remaining_total)]

            for i in range(1, maxChoosableInteger + 1):
                if (mask >> (i - 1)) & 1:
                    if i >= remaining_total:
                        memo[(mask, remaining_total)] = True
                        return True
                    
                    if not can_win(mask ^ (1 << (i - 1)), remaining_total - i):
                        memo[(mask, remaining_total)] = True
                        return True
            
            memo[(mask, remaining_total)] = False
            return False

        initial_mask = (1 << maxChoosableInteger) - 1
        return can_win(initial_mask, desiredTotal)

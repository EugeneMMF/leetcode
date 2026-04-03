class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        deleted_columns_count = 0
        
        for j in range(num_cols):
            for i in range(num_rows - 1):
                if strs[i][j] > strs[i+1][j]:
                    deleted_columns_count += 1
                    break
                    
        return deleted_columns_count

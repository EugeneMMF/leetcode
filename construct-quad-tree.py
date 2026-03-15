
class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        n = len(grid)

        def _construct_recursive(row_start, col_start, length):
            first_val = grid[row_start][col_start]
            is_homogeneous = True
            for r in range(row_start, row_start + length):
                for c in range(col_start, col_start + length):
                    if grid[r][c] != first_val:
                        is_homogeneous = False
                        break
                if not is_homogeneous:
                    break
            
            if is_homogeneous:
                return Node(val=bool(first_val), isLeaf=True)
            
            node_val = True 
            is_leaf = False
            
            half_length = length // 2
            
            topLeft = _construct_recursive(row_start, col_start, half_length)
            topRight = _construct_recursive(row_start, col_start + half_length, half_length)
            bottomLeft = _construct_recursive(row_start + half_length, col_start, half_length)
            bottomRight = _construct_recursive(row_start + half_length, col_start + half_length, half_length)
            
            return Node(node_val, is_leaf, topLeft, topRight, bottomLeft, bottomRight)
        
        return _construct_recursive(0, 0, n)

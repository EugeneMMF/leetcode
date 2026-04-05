class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = []
        current_label = label

        while current_label >= 1:
            path.append(current_label)

            if current_label == 1:
                break

            row_L = current_label.bit_length()

            if row_L % 2 == 1:
                standard_parent_val = current_label // 2

                parent_row = row_L - 1
                min_parent_row_val = 1 << (parent_row - 1)
                max_parent_row_val = (1 << parent_row) - 1
                
                current_label = min_parent_row_val + max_parent_row_val - standard_parent_val
            else:
                min_curr_row_val = 1 << (row_L - 1)
                max_curr_row_val = (1 << row_L) - 1
                
                standard_curr_label = min_curr_row_val + max_curr_row_val - current_label
                
                current_label = standard_curr_label // 2
        
        path.reverse()
        return path

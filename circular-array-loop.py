class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def get_next_index(current_idx, is_forward_direction_for_path):
            val = nums[current_idx]
            
            if val == 0 or (val > 0) != is_forward_direction_for_path:
                return -1

            next_idx = (current_idx + val) % n
            
            if next_idx == current_idx:
                return -1
            
            return next_idx

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            is_forward = (nums[i] > 0)

            while True:
                slow = get_next_index(slow, is_forward)
                fast = get_next_index(fast, is_forward)
                
                if slow == -1 or fast == -1:
                    break
                
                fast = get_next_index(fast, is_forward)
                if fast == -1:
                    break

                if slow == fast:
                    return True
            
            curr = i
            while True:
                next_node_val = nums[curr]
                if next_node_val == 0 or (next_node_val > 0) != is_forward:
                    break
                
                next_idx = (curr + next_node_val) % n
                
                if next_idx == curr:
                    nums[curr] = 0
                    break
                
                nums[curr] = 0
                curr = next_idx

        return False

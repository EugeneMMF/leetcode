class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        max_ends_at_start_point = [0] * (time + 1)
        for s, e in clips:
            if s <= time:
                max_ends_at_start_point[s] = max(max_ends_at_start_point[s], e)
        
        num_clips = 0
        current_reach = 0
        farthest_reach = 0

        for i in range(time + 1):
            farthest_reach = max(farthest_reach, max_ends_at_start_point[i])

            if i == current_reach:
                if current_reach == time:
                    break
                
                if farthest_reach <= current_reach:
                    return -1

                num_clips += 1
                current_reach = farthest_reach
            
            if current_reach >= time:
                break
        
        return num_clips if current_reach >= time else -1

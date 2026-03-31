class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counts = {}
        for x in answers:
            counts[x] = counts.get(x, 0) + 1
            
        total_rabbits = 0
        
        for ans_val, freq in counts.items():
            group_size = ans_val + 1
            
            num_groups = (freq + group_size - 1) // group_size
            
            total_rabbits += num_groups * group_size
            
        return total_rabbits

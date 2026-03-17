class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        
        outcomes_per_pig = rounds + 1
        
        pigs = 0
        total_possible_outcomes = 1
        
        while total_possible_outcomes < buckets:
            total_possible_outcomes *= outcomes_per_pig
            pigs += 1
            
        return pigs

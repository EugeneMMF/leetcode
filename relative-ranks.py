class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        
        # Create a list of tuples (score, original_index)
        indexed_scores = []
        for i in range(n):
            indexed_scores.append((score[i], i))
            
        # Sort the athletes by their scores in descending order
        indexed_scores.sort(key=lambda x: x[0], reverse=True)
        
        # Initialize the result array
        answer = [""] * n
        
        # Assign ranks based on sorted order
        for i, (current_score, original_index) in enumerate(indexed_scores):
            placement = i + 1 # 1-based placement
            
            if placement == 1:
                rank_str = "Gold Medal"
            elif placement == 2:
                rank_str = "Silver Medal"
            elif placement == 3:
                rank_str = "Bronze Medal"
            else:
                rank_str = str(placement)
            
            # Place the rank in the correct position in the answer array
            answer[original_index] = rank_str
            
        return answer

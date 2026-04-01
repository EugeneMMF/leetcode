class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        forces_R = [float('inf')] * n
        current_R_dist = float('inf')
        for i in range(n):
            if dominoes[i] == 'R':
                current_R_dist = 0
            elif dominoes[i] == 'L':
                current_R_dist = float('inf')
            elif current_R_dist != float('inf'):
                current_R_dist += 1
            forces_R[i] = current_R_dist
            
        forces_L = [float('inf')] * n
        current_L_dist = float('inf')
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                current_L_dist = 0
            elif dominoes[i] == 'R':
                current_L_dist = float('inf')
            elif current_L_dist != float('inf'):
                current_L_dist += 1
            forces_L[i] = current_L_dist
            
        result = list(dominoes)
        for i in range(n):
            if dominoes[i] == '.':
                dist_R = forces_R[i]
                dist_L = forces_L[i]
                
                if dist_R == float('inf') and dist_L == float('inf'):
                    result[i] = '.'
                elif dist_R == float('inf'):
                    result[i] = 'L'
                elif dist_L == float('inf'):
                    result[i] = 'R'
                elif dist_R < dist_L:
                    result[i] = 'R'
                elif dist_L < dist_R:
                    result[i] = 'L'
                else:
                    result[i] = '.'
                    
        return "".join(result)


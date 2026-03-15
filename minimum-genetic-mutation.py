from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0

        valid_genes = set(bank)

        if endGene not in valid_genes:
            return -1

        char_choices = ['A', 'C', 'G', 'T']
        
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            current_gene, mutations_count = queue.popleft()

            if current_gene == endGene:
                return mutations_count

            for i in range(len(current_gene)):
                original_char = current_gene[i]
                for char in char_choices:
                    if char == original_char:
                        continue
                    
                    next_gene = current_gene[:i] + char + current_gene[i+1:]

                    if next_gene in valid_genes and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations_count + 1))
        
        return -1

import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        in_degree = [0] * n

        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1
        
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                if root != -1:
                    return False
                root = i
            elif in_degree[i] > 1:
                return False
        
        if root == -1:
            return False
            
        q = collections.deque([root])
        visited_count = 0
        
        visited = {root}

        while q:
            node = q.popleft()
            visited_count += 1
            
            left_child_node = leftChild[node]
            if left_child_node != -1:
                if left_child_node in visited:
                    return False
                visited.add(left_child_node)
                q.append(left_child_node)
            
            right_child_node = rightChild[node]
            if right_child_node != -1:
                if right_child_node in visited:
                    return False
                visited.add(right_child_node)
                q.append(right_child_node)
        
        return visited_count == n


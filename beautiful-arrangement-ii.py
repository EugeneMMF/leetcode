from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = []
        
        left = 1
        right = k + 1
        
        for i in range(k + 1):
            if i % 2 == 0:
                answer.append(left)
                left += 1
            else:
                answer.append(right)
                right -= 1
        
        for num in range(k + 2, n + 1):
            answer.append(num)
            
        return answer
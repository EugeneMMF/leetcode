from typing import List

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        max_bit = k.bit_length()
        next_node = [[0]*max_bit for _ in range(n)]
        sum_node = [[0]*max_bit for _ in range(n)]
        for i in range(n):
            next_node[i][0] = receiver[i]
            sum_node[i][0] = receiver[i]
        for b in range(1, max_bit):
            for i in range(n):
                nxt = next_node[i][b-1]
                next_node[i][b] = next_node[nxt][b-1]
                sum_node[i][b] = sum_node[i][b-1] + sum_node[nxt][b-1]
        max_score = 0
        for i in range(n):
            cur = i
            total = i
            rem = k
            bit = 0
            while rem:
                if rem & 1:
                    total += sum_node[cur][bit]
                    cur = next_node[cur][bit]
                rem >>= 1
                bit += 1
            if total > max_score:
                max_score = total
        return max_score

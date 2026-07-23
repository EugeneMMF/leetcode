
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            count0 = count1 = 0
            for j in range(i, n):
                if s[j] == '0':
                    count0 += 1
                else:
                    count1 += 1
                if count0 > k and count1 > k:
                    break
                count += 1
        return count

        

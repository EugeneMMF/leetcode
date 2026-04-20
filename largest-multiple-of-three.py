from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = [0] * 10
        total = 0
        for d in digits:
            cnt[d] += 1
            total += d
        mod = total % 3
        def remove_one(rem):
            for i in range(1, 10):
                if i % 3 == rem and cnt[i]:
                    cnt[i] -= 1
                    return True
            return False
        def remove_two(rem):
            removed = 0
            for i in range(1, 10):
                while i % 3 == rem and cnt[i] and removed < 2:
                    cnt[i] -= 1
                    removed += 1
                    if removed == 2:
                        return True
            return False
        if mod == 1:
            if not remove_one(1):
                if not remove_two(2):
                    return ""
        elif mod == 2:
            if not remove_one(2):
                if not remove_two(1):
                    return ""
        res = []
        for i in range(9, -1, -1):
            res.append(str(i) * cnt[i])
        ans = ''.join(res)
        if not ans:
            return ""
        if ans[0] == '0':
            return "0"
        return ans

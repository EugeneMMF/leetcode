class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(target):
            left = 0
            max_len = 0
            changes = 0
            for right, ch in enumerate(answerKey):
                if ch != target:
                    changes += 1
                while changes > k:
                    if answerKey[left] != target:
                        changes -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len
        return max(helper('T'), helper('F'))

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        answer = []
        current_remainder = 0
        for num in nums:
            current_remainder = (current_remainder * 2 + num) % 5
            answer.append(current_remainder == 0)
        return answer

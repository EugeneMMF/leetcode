class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = -1
        for i in range(len(number)-1):
            if number[i] == digit and number[i] < number[i+1]:
                idx = i
                break
        if idx == -1:
            idx = number.rfind(digit)
        return number[:idx] + number[idx+1:]

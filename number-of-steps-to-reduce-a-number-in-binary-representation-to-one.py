class Solution:
    def numSteps(self, s: str) -> int:
        bits = list(s)
        steps = 0
        while not (len(bits) == 1 and bits[0] == '1'):
            if bits[-1] == '0':
                bits.pop()
                steps += 1
            else:
                i = len(bits) - 1
                while i >= 0 and bits[i] == '1':
                    bits[i] = '0'
                    i -= 1
                if i < 0:
                    bits = ['1'] + bits
                else:
                    bits[i] = '1'
                steps += 1
        return steps
